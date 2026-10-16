# Release notes

## 0.9.1 beta (16 October 2026)

**From this version on, Rindi-Agent updates itself.** If you have 0.9.0, download 0.9.1 once and replace the app in Applications.

- **In-app updates.** Rindi-Agent checks for new versions once a day, and **Rindi-Agent › Check for Updates…** checks right away. Updates are signed and install with one click. **Settings › About** turns automatic checks on or off.
- **Flash Next with refusal directions** in Model Setup: the same weights, plus the file that the optional **Settings › General › Refusal ablation** setting needs, for security and red-team lab work. The setting is off by default.
- **Fix:** **Reveal Rindi Computer Use** in the Computer Use window now shows the helper inside the app, for adding it to Screen Recording.
- **Fix:** the `.sha256` checksum file contains only the file name, so `shasum -c` works after downloading.

## 0.9.0 beta (16 October 2026)

The first public beta.

- A coding agent that reads, edits and tests code in your project, with every change and command waiting for your approval by default
- Computer Use: the agent can read and operate native Mac apps through Accessibility, in the background, while you watch in a picture-in-picture window
- Source control, files, terminal, a built-in browser, and a task board with worker agents
- MCP servers, global instructions and skills, voice input and spoken replies
