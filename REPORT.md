# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

<!-- Paste the agent's response to "What is the agentic loop?" and "What labs are available in our LMS?" -->
The agentic loop is the fundamental cycle that autonomous AI agents follow to perceive, reason, and act. It's the core pattern that enables agents to work   
independently toward goals.

The Basic Loop


 ┌─────────────┐
 │  PERCEIVE   │ ──→ Gather information from environment
 └──────┬──────┘     (observations, user input, tool outputs)
        │
        ▼
 ┌─────────────┐
 │   REASON    │ ──→ Process information, plan next steps
 └──────┬──────┘     (analyze, decide, strategize)
        │
        ▼
 ┌─────────────┐
 │    ACT      │ ──→ Execute actions via tools
 └──────┬──────┘     (call APIs, write files, run commands)
        │
        ▼
        └──────────→ Loop back to PERCEIVE


Key Components

 1 Perceive — Observe the current state (user requests, file contents, command outputs, web results)
 2 Reason — Interpret observations, recall relevant knowledge, plan actions, evaluate options
 3 Act — Execute chosen actions through available tools (file operations, web searches, shell commands, etc.)
 4 Reflect (optional) — Evaluate outcomes, learn from mistakes, adjust strategy

Why It Matters

 • Autonomy: The loop enables agents to work without constant human guidance
 • Adaptability: Agents can respond to changing conditions and unexpected results
 • Goal-directed behavior: Each iteration moves closer to completing objectives
 • Tool use: Agents extend their capabilities by calling external tools

In my case, I follow this loop continuously: I read your request (perceive), think about how to help (reason), call tools if needed (act), and then report   
back or continue iterating.

Is there a specific aspect of the agentic loop you'd like to explore further?


Based on the course documentation, here are the 10 labs available in your LMS (SET course):

Available Labs

The course consists of 10 labs, each 3 hours long. From the documentation, I can see details about:

Lab 8 (Current) — "The Agent is the Interface"

Topic: AI agents as a new type of client interface for existing services

Learning outcomes:

 • Understand how AI agents differ from traditional clients (web apps, bots)
 • Set up nanobot from scratch with MCP tools
 • Give the agent observability capabilities (logs, traces)
 • Diagnose failures and make the agent proactive with scheduled health checks

Key tasks:

 1 Set up the Agent (install nanobot, connect to Qwen API, add LMS tools, write skill prompts)
 2 Deploy the Agent and add a Web Client (Docker, WebSocket, Flutter client)
 3 Give the Agent New Eyes (observability tools for VictoriaLogs and VictoriaTraces)
 4 Diagnose a Failure and Make the Agent Proactive (multi-step investigation, cron scheduling, bug fix)

Optional: Add a Telegram Bot Client

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Previous Labs Referenced:

 • Lab 6 — Earlier setup (mentioned in setup adjustments)
 • Lab 7 — Built a Telegram bot with hardcoded slash commands and manual tool-calling loop

-------------------------------------------------------------------------------------------------------------------------------------------------------------
The full list of all 10 lab titles isn't explicitly documented in the files I found, but the course structure shows this is a progressive curriculum where   
students build up from basic VM setup → web app → Telegram bot → AI agent with observability.

Would you like me to search for more specific information about other labs, or help you with something related to Lab 8?

## Task 1B — Agent with LMS tools

<!-- Paste the agent's response to "What labs are available?" and "Describe the architecture of the LMS system" -->
Based on the LMS system, here are the available labs:


 ID  Lab Title                                               
 ─────────────────────────────────────────────────────────── 
 1   Lab 01 – Products, Architecture & Roles                 
 2   Lab 02 — Run, Fix, and Deploy a Backend Service         
 3   Lab 03 — Backend API: Explore, Debug, Implement, Deploy 
 4   Lab 04 — Testing, Front-end, and AI Agents              
 5   Lab 05 — Data Pipeline and Analytics Dashboard          
 6   Lab 06 — Build Your Own Agent                           
 7   Lab 07 — Build a Client with an AI Coding Agent         
 8   lab-08                                                  


There are 8 labs available. Would you like to see scores, pass rates, or other details for any specific lab?

Yes, the LMS backend is healthy. It currently contains 56 items.

## Task 1C — Skill prompt

<!-- Paste the agent's response to "Show me the scores" (without specifying a lab) -->
Which lab would you like to see the scores for? Here are the available labs:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 Lab 08 — lab-08

Please let me know which lab you're interested in, or I can show you pass rates, completion rates, top learners, or group performance for a specific lab.

## Task 2A — Deployed agent

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->
nanobot-1  | Using config: /tmp/nanobot/config.resolved.json
nanobot-1  | Using config: /tmp/nanobot/config.resolved.json
nanobot-1  | 🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
nanobot-1  | 2026-03-30 15:05:26.484 | DEBUG    | nanobot.channels.registry:discover_all:64 - Skipping built-in channel 'matrix': Matrix dependencies not installed. Run: pip install nanobot-ai[matrix]
nanobot-1  | 2026-03-30 15:05:27.053 | INFO     | nanobot.channels.manager:_init_channels:58 - WebChat channel enabled
nanobot-1  | ✓ Channels enabled: webchat
nanobot-1  | ✓ Heartbeat: every 1800s
nanobot-1  | 2026-03-30 15:05:27.055 | INFO     | nanobot.cron.service:_load_store:85 - Cron: jobs.json modified externally, reloading
nanobot-1  | 2026-03-30 15:05:27.056 | INFO     | nanobot.cron.service:start:202 - Cron service started with 0 jobs
nanobot-1  | 2026-03-30 15:05:27.056 | INFO     | nanobot.heartbeat.service:start:124 - Heartbeat started (every 1800s)
nanobot-1  | 2026-03-30 15:05:27.432 | INFO     | nanobot.channels.manager:start_all:91 - Starting webchat channel...
nanobot-1  | 2026-03-30 15:05:27.433 | INFO     | nanobot.channels.manager:_dispatch_outbound:119 - Outbound dispatcher started
nanobot-1  | 2026-03-30 15:05:29.105 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_health' from server 'lms'nanobot-1  | 2026-03-30 15:05:29.105 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_labs' from server 'lms'  
nanobot-1  | 2026-03-30 15:05:29.105 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_learners' from server 'lms'
nanobot-1  | 2026-03-30 15:05:29.105 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_pass_rates' from server 'lms'
nanobot-1  | 2026-03-30 15:05:29.105 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_timeline' from server 'lms'
nanobot-1  | 2026-03-30 15:05:29.105 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_groups' from server 'lms'nanobot-1  | 2026-03-30 15:05:29.105 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_top_learners' from server 'lms'
nanobot-1  | 2026-03-30 15:05:29.105 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_completion_rate' from server 'lms'
nanobot-1  | 2026-03-30 15:05:29.105 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_sync_pipeline' from server 'lms'
nanobot-1  | 2026-03-30 15:05:29.105 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'lms': connected, 9 tools registered
nanobot-1  | 2026-03-30 15:05:29.105 | INFO     | nanobot.agent.loop:run:280 - Agent loop started

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->
![alt text](sreenshotes/image.png)
![alt text](sreenshotes/image-1.png)
![alt text](sreenshotes/image-2.png)

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

backend-1  | 2026-03-30 15:26:39,930 INFO [httpx] [_client.py:1740] [trace_id=c238e3e92b32f766d1b1b075fd28d1e6 span_id=72adb02d67e920c9 resource.service.name=Learning Management Service trace_sampled=True] - HTTP Request: GET https://auche.namaz.live/api/logs?limit=500&since=2026-03-21T15%3A30%3A32.373603 "HTTP/1.1 200 OK"

backend-1  | INFO:     172.18.0.9:44614 - "GET /items/ HTTP/1.1" 404
backend-1  | INFO:     172.18.0.9:44614 - "GET /items/ HTTP/1.1" 404 Not Found

![alt text](sreenshotes/image-3.png)

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

![alt text](sreenshotes/image-4.png)
![alt text](sreenshotes/image-6.png)

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

**Good news!** The LMS backend is currently healthy. Here's what I found:

**LMS Health Status:**
- Status: ✅ Healthy
- Item count: 56
- Errors: None reported

**Recent Traces:**
The most recent traces show the service is operating normally. There were 2 error traces around 16:02 (about 29 minutes ago), but those are outside your 10-minute window. No errors appear in the more recent activity.

**Note:** The log search tool is experiencing query syntax issues with VictoriaLogs, but the health check and trace data both indicate the LMS backend has been running without errors in the last 10 minutes.

Would you like me to investigate those earlier errors from 16:02, or check anything else about the LMS?

## Summary for LMS Backend (Last 10 Minutes)

**Good news:** No errors detected in the last 10 minutes based on trace data.

**Current Status:**
- **LMS Health:** ⚠️ Unhealthy (HTTP 404)
- **Recent Traces:** The most recent trace at 16:31:26 (~4 min ago) completed successfully with status "ok"
- **Error Traces:** 2 errors occurred ~33 minutes ago (16:02:51-52) due to a connection issue ("Name or service not known"), but nothing in the last 10 minutes

**Note:** The logs search is currently returning 400 errors from VictoriaLogs, so I couldn't query detailed log messages. However, the trace data shows no recent errors.

Would you like me to investigate the current unhealthy status further or check specific trace details?

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
