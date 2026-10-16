# Release notes

## 0.9.2 beta (16 October 2026)

- **Fix:** Rindi-Agent could crash while the agent was working and the pointer was over its window. The cause is a bug in macOS 27's Swift runtime; Rindi-Agent now works around it at the point where the crash happened.

If you have 0.9.1, Rindi-Agent offers this update by itself; you can also choose **Rindi-Agent › Check for Updates…**. If you have 0.9.0, download it once from the releases page.

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
