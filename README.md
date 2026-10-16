# Rindi-Agent

Rindi-Agent is a coding agent for the Mac that runs Qwen 3.8 models entirely on your computer. The model, your code and your conversations stay on the machine: there is no account, no cloud service and no local server to run.

![Rindi-Agent fixing a failing test in a small Python project](docs/images/03-conversation.png)

> **This is a beta.** Expect rough edges, and please [report what you find](#reporting-problems).

## Download

**[Download Rindi-Agent 0.9.0 beta](https://github.com/True2456/Rindi-Agent-releases/releases/tag/v0.9.0-beta)**: a 54 MB disk image, signed and notarized by Apple. The model is downloaded separately the first time you open the app.

To check the download, put the `.dmg` and its `.sha256` file in the same folder and run:

```bash
shasum -a 256 -c Rindi-Agent-0.9.0.dmg.sha256
```

It prints `Rindi-Agent-0.9.0.dmg: OK` when the file is intact.

## Requirements

- A Mac with Apple silicon running **macOS 27** or later
- Enough unified memory and disk space for the model you choose:

  | Model | Download | Memory | Best for |
  | --- | --- | --- | --- |
  | Qwen 3.8 Flash Next (4-bit) | 182 GB | 128 GB | Long coding sessions, up to 256k tokens of context |
  | Qwen 3.8 27B (AWQ 5.0 bpw) | 17 GB | 32 GB | Smaller Macs; text, images and video |
  | Qwen 3.8 27B (AWQ 4.85 bpw) | 17 GB | 32 GB | A slightly smaller 27B build |

Without a downloaded model, Rindi-Agent can use Apple's on-device model for short conversations.

## Install

1. Open `Rindi-Agent-0.9.0.dmg` and drag **Rindi-Agent** onto **Applications**.
2. Open Rindi-Agent from your Applications folder. macOS asks once whether to open an app downloaded from the internet; choose **Open**.
3. In **Set up a model**, choose **Download** on the model that fits your Mac, or **Use Custom Folder…** if you already have it.
4. Choose **File › Open Workspace** (⌘O), pick a project folder, and describe what you want done.

The [User Guide](docs/USER-GUIDE.md) walks through everything else, with screenshots: sessions, approvals, the side panels, Computer Use, settings and troubleshooting.

## What it can do

- **Work on your code.** Reads, searches, edits and patches files in the workspace, and runs commands in a sandbox. In the default **Approve** mode, every change and command waits for you.
- **Use your Mac's apps.** Computer Use lets the agent read and operate native apps through Accessibility, in the background, without moving your cursor or taking focus. You watch it in a small picture-in-picture window.
- **Keep you in the loop.** Source control with staging, commits and branches; a file browser; long-running processes with live logs; a built-in web browser; and a task board where the agent can hand cards to worker agents.
- **Extend it.** Global instructions, reusable skills, and Model Context Protocol (MCP) servers.
- **Talk to it.** On-device voice input, and spoken replies with your installed voices.

## Privacy

Rindi-Agent uses the network only to:

- download models from huggingface.co,
- search the web and read pages, when the agent uses its web tools,
- reach MCP servers you add yourself.

Everything else, including inference, happens on your Mac.

## Updating

There is no automatic update in this beta. To update, download the new disk image and replace the app in Applications. Your settings, chats, models and macOS permissions are kept.

## Reporting problems

Open an issue in this repository with:

- what you did and what happened,
- your Mac model, memory and macOS version,
- the runtime log: **Settings › About › Runtime log › Reveal**, or `~/Library/Logs/Rindi-Agent/runtime.log`.

Check the log for anything private before you attach it: it can include file names from your projects.
