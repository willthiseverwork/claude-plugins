# Directories Done

Directories Done prepares and runs free directory listings for a live product, tool or site. It builds a source-faithful listing kit, gets one approval for the kit and proposed sites, prevents duplicates, uses only free submission routes, and verifies every submitted or edited listing afterward. It separates launch platforms and editorial outreach from normal directory submissions.

The plugin contains no accounts, contact data, product listing statuses, or default brand details. It reads a local `defaults.local.md` only when its installer has supplied one; that file must stay outside any public repository or uploaded plugin package.

## Install in Claude Code

```text
/plugin marketplace add willthiseverwork/claude-plugins
/plugin install directories-done@willthiseverwork
```

Start a new Claude Code session after installation.

## Install in Codex

Copy the `directories-done` folder into your Codex skills directory, then start a new Codex task. For a user-level installation, the destination is normally:

```text
~/.codex/skills/directories-done
```

Keep any `defaults.local.md` in that installed plugin folder only; do not commit it. Codex will load the skill when a user asks to list a released product, tool, or site in directories.

## Use it

Ask for directory listings for a live product. Directories Done first makes a listing kit from the live site and shows its text counts, square logo sizes and proposed directory list. After one approval, it can submit or edit the approved free listings, then reports live, pending, needs-you and skipped results.
