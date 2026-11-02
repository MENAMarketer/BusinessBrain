---
name: write
description: Copywriter. Writes posts, pages and emails from the Business File and Voice File, then turns feedback into updates to both files. Use for /brain:write or any request for content.
---

# Business Brain: Write

Run the Copywriter.

Read the agent file at `1 Agents/3 Copywriter.md` in this plugin's root folder (two folders up from this skill's folder) and follow it exactly, step by step, including its questions. That file is the agent; this skill only opens it.

The person's own files live in their working folder: the Business File in `2 My Business`, the Voice File in `3 My Voice`, drafts in `4 Content`, other material in `5 Library`. Read them there, ignore any file whose name starts with "Blank", and write updated files back to the same folders when the agent says to save them, after showing the person what changed.

In this plugin the commands are /brain:start, /brain:research, /brain:tone, /brain:write and /brain:optimise. Where an agent file says "/research", "/tone", "/write" or "/optimise", tell the person the /brain: version.
