# Setup for Claude

About five minutes. Do this on a laptop, signed in to claude.ai.

1. Click **Projects** in the left sidebar, then **New project**.
2. Name it after your business, for example "Harbour & Co AI System".
3. Find the project's **instructions** and paste in everything below the line in *Project Instructions.md*. Replace [Business name] with yours.
4. Find the project's **files** (project knowledge) and add all five files from the *1 Agents* folder. Do not add the blank templates.
5. Start a new chat inside the project and type **research** followed by your website address. The slash is optional: if typing "/" opens a menu, just leave it out.

## As you go

- When an agent gives you a **Business File** or **Voice File**, save it in your *Business Brain* folder (*2 My Business* or *3 My Voice*). Before your next chat, add it to the project's files.
- When an agent gives you an **updated** file, delete the old one from the project's files and add the new one.
- Start a fresh chat inside the project for each new piece of work. The files carry the memory, so nothing is lost.

## If it cannot read your website

Some assistants can read websites and some cannot, depending on your plan and settings. If it says it cannot, copy the text of your home page and about page and paste it in. The result is the same.

## Or install it as a plugin

If you use Claude Code or the Claude desktop app with plugins, you can install Business Brain once and use it in any folder.

1. Add the marketplace: `/plugin marketplace add MENAMarketer/BusinessBrain`
2. Install it: `/plugin install brain@businessbrain`
3. Open your **Business Brain** folder and type **/brain:start**.

The commands become **/brain:start**, **/brain:research**, **/brain:tone**, **/brain:write** and **/brain:optimise**. The agents read and save your files straight into your folders, so there is nothing to upload.

**Adding your own agent with the plugin:** save it in the *1 Agents* folder of your Business Brain folder, then type **/brain:start** followed by its name, for example "/brain:start Pitch Builder".
