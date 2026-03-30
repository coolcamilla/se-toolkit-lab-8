# Observability Skill

You have access to observability tools that can query VictoriaLogs and VictoriaTraces. Use these tools to investigate system health, errors, and request traces.

## Available Tools

### Log Tools (VictoriaLogs)

- **`mcp_obs_logs_search`** — Search logs using LogsQL queries
  - Use for finding specific events, errors, or patterns
  - Time range: use `start_time` and `end_time` in RFC3339 format (e.g., `2026-03-30T10:00:00Z`)
  - Default limit: 100 entries
  - Example query: `service.name:"Learning Management Service" severity:ERROR`

- **`mcp_obs_logs_error_count`** — Count errors per service
  - Use as first step when asked about errors
  - Returns count grouped by service
  - Default time window: 1 hour

### Trace Tools (VictoriaTraces)

- **`mcp_obs_traces_list`** — List recent traces for a service
  - Returns trace summaries with: trace_id, duration, span_count, status (ok/error)
  - Default service: "Learning Management Service"
  - Use to find traces to investigate

- **`mcp_obs_traces_get`** — Get full trace details by ID
  - Returns complete span hierarchy with errors highlighted
  - Use after finding a trace_id from logs_search or traces_list

## Workflow

### When asked about errors:

1. **Start with `logs_error_count`** to see if there are recent errors and which services are affected
2. **Use `logs_search`** to find specific error logs for the affected service
   - Extract `trace_id` from error logs if present
3. **Use `traces_get`** to investigate the full request flow if you found a trace_id
4. **Summarize findings** — don't dump raw JSON

### When asked about a specific request:

1. **Use `logs_search`** with the trace_id or time range
2. **Use `traces_get`** to see the full span hierarchy
3. **Identify bottlenecks** — look for spans with long durations
4. **Check for errors** — look for `error: true` tags or exception logs

### When asked about system health:

1. **Check error count** — `logs_error_count` for the last hour
2. **Check recent traces** — `traces_list` to see status distribution
3. **Summarize** — "X errors in the last hour, mostly from service Y"

## Query Examples

### Find LMS backend errors in the last 10 minutes:
```
logs_error_count(service="Learning Management Service", hours=0.17)
```

### Search for specific error pattern:
```
logs_search(query='service.name:"Learning Management Service" severity:ERROR', limit=50)
```

### Find traces with errors:
```
traces_list(service="Learning Management Service", limit=20)
# Then fetch traces with status="error"
traces_get(trace_id="<trace_id_from_list>")
```

## Response Guidelines

- **Be concise** — summarize findings, don't dump raw JSON
- **Highlight errors** — if found, explain what went wrong
- **Include trace_id** — when referencing specific requests
- **Time context** — mention the time window you searched
- **Actionable** — if you find errors, suggest what might be wrong

### Good response example:
> "Found 3 errors in the Learning Management Service in the last 10 minutes. All errors are 'Name or service not known' when connecting to PostgreSQL. This suggests the database service was unavailable. Trace ID: 2e282ae8e5702832657ffbec701963cf shows the connection failed after 197ms."

### Bad response example:
> [Dumps entire JSON response from logs_search without any summary]
