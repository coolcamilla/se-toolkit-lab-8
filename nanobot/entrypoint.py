#!/usr/bin/env python3
"""
Entrypoint script for nanobot Docker container.

Reads config.json, injects environment variable values, writes config.resolved.json,
then execs into nanobot gateway.
"""

import json
import os
import sys


def main():
    # Paths
    config_path = "/app/nanobot/config.json"
    # Write resolved config to /tmp to avoid permission issues when
    # container runs as host user but image files are owned by appuser
    resolved_path = "/tmp/nanobot/config.resolved.json"
    workspace = "/app/nanobot/workspace"

    # Ensure directory exists
    os.makedirs(os.path.dirname(resolved_path), exist_ok=True)

    # Read base config
    with open(config_path, "r") as f:
        config = json.load(f)

    # Override provider settings from env vars
    if llm_api_key := os.environ.get("LLM_API_KEY"):
        config["providers"]["custom"]["apiKey"] = llm_api_key

    if llm_api_base_url := os.environ.get("LLM_API_BASE_URL"):
        config["providers"]["custom"]["apiBase"] = llm_api_base_url

    # Override agent defaults
    if llm_api_model := os.environ.get("LLM_API_MODEL"):
        config["agents"]["defaults"]["model"] = llm_api_model

    # Override gateway settings
    if nanobot_gateway_host := os.environ.get("NANOBOT_GATEWAY_CONTAINER_ADDRESS"):
        config["gateway"]["host"] = nanobot_gateway_host

    if nanobot_gateway_port := os.environ.get("NANOBOT_GATEWAY_CONTAINER_PORT"):
        config["gateway"]["port"] = int(nanobot_gateway_port)

    # Override LMS MCP server settings
    if nanobot_lms_backend_url := os.environ.get("NANOBOT_LMS_BACKEND_URL"):
        config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_BACKEND_URL"] = (
            nanobot_lms_backend_url
        )

    if nanobot_lms_api_key := os.environ.get("NANOBOT_LMS_API_KEY"):
        config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_API_KEY"] = (
            nanobot_lms_api_key
        )

    # Write resolved config
    with open(resolved_path, "w") as f:
        json.dump(config, f, indent=2)

    print(f"Using config: {resolved_path}", file=sys.stderr)

    # Exec into nanobot gateway
    os.execvp(
        "nanobot",
        [
            "nanobot",
            "gateway",
            "--config",
            resolved_path,
            "--workspace",
            workspace,
        ],
    )


if __name__ == "__main__":
    main()
