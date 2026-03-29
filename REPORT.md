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

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
