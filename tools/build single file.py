# Builds "Business Brain.md" at the repo root from the header and the agent files in "1 Agents".
# The agent files stay the single source; run this after editing any of them.
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent

def demote(text, by):
    out, fence = [], False
    for line in text.split("\n"):
        if line.startswith("```"): fence = not fence
        elif not fence and re.match(r"#+ ", line): line = "#" * by + line
        out.append(line)
    return "\n".join(out)

parts = [(root / "tools" / "single file header.md").read_text().rstrip("\n-") + "\n"]
agents = [("1 Research Agent.md", "research"), ("2 Tone Agent.md", "tone"), ("3 Copywriter.md", "write"),
          ("4 Optimiser.md", "optimise")]
for f, cmd in agents:
    body = re.sub(r"\A---\n.*?\n---\n", "", (root / "1 Agents" / f).read_text(), flags=re.S).strip()
    parts.append(f"---\n\n<!-- Command: {cmd} -->\n" + demote(body, 1) + "\n")
tmpl = re.sub(r"\A---\n.*?\n---\n", "", (root / "1 Agents" / "New Agent Template.md").read_text(), flags=re.S).strip()
parts.append("---\n\n<!-- Command: new agent -->\n## Agent Builder\n\nWhen they type **new agent**, interview them one question at a time to fill in the template below. "
             "Then give them the finished agent as a file named after it, and tell them to attach it alongside Business Brain.md from now on.\n\n"
             "### The template\n\n" + demote(tmpl, 3) + "\n")
out = "\n".join(parts)
(root / "Business Brain.md").write_text(out)
print(len(out), "characters written to Business Brain.md")
