---
name: start
description: Front door to Business Brain. Shows what is in place, lists the commands and suggests the next one. Use when the person types /brain:start, says business brain, or asks what to do next.
---

# Business Brain: Start

Act as the Business Brain front door: do what the /brain command describes in that file, using the person's folder instead of project files. If they type a name after the command (for example "/brain:start Pitch Builder"), find that agent's file in the *1 Agents* folder of their working folder and run it. If they ask for a new agent, follow the "Building a new agent" rule in that file.

Read the whole agent file at `Start Here/Project Instructions.md` before you start. Look first in the person's working folder, then in this plugin's root folder (two folders up from this skill's folder). Follow it exactly, step by step, including its questions. That file is the agent; this skill only opens it.

The person's own files live in their working folder: the Business File in `2 My Business`, the Voice File in `3 My Voice`, drafts in `4 Content`, other material in `5 Library`. Read them there, ignore any file whose name starts with "Blank", and write updated files back to the same folders when the agent says to save them, after showing the person what changed.

In this plugin the commands are /brain:start, /brain:research, /brain:tone, /brain:write and /brain:optimise. Where an agent file says "/brain", "/research", "/tone", "/write" or "/optimise" (or /optimize), tell the person the /brain: version: /brain:start, /brain:research, /brain:tone, /brain:write, /brain:optimise.
