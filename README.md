# Rindi-Agent

Rindi-Agent is a coding agent for the Mac that runs Qwen 3.8 models entirely on your computer. The model, your code and your conversations stay on the machine: there is no account, no cloud service and no local server to run.

![Rindi-Agent fixing a failing test in a small Python project](docs/images/03-conversation.png)

> **This is a beta.** Expect rough edges, and please [report what you find](#reporting-problems).

## Download

**[Download Rindi-Agent 0.9.2 beta](https://github.com/True2456/Rindi-Agent-releases/releases/tag/v0.9.2-beta)**: a 55 MB disk image, signed and notarized by Apple. The model is downloaded separately the first time you open the app. Starting with 0.9.1, Rindi-Agent updates itself.

To check the download, put the `.dmg` and its `.sha256` file in the same folder and run:

```bash
shasum -a 256 -c Rindi-Agent-0.9.2.dmg.sha256
```

It prints `Rindi-Agent-0.9.2.dmg: OK` when the file is intact.

## Requirements

- A Mac with Apple silicon running **macOS 27** or later
- Enough unified memory and disk space for the model you choose:

  | Model | Download | Memory | Best for |
  | --- | --- | --- | --- |
  | Qwen 3.8 Flash Next (4-bit) | 182 GB | 128 GB | Long coding sessions, up to 256k tokens of context |
  | Qwen 3.8 27B (AWQ 5.0 bpw) | 17 GB | 32 GB | Smaller Macs; text, images and video |
  | Qwen 3.8 27B (AWQ 4.85 bpw) | 17 GB | 32 GB | A slightly smaller 27B build |

  Flash Next also comes in a version **with refusal directions**: the same weights, plus the file that the optional *Refusal ablation* setting needs (see the [User Guide](docs/USER-GUIDE.md#refusal-ablation)).

Without a downloaded model, Rindi-Agent can use Apple's on-device model for short conversations.

## Install

1. Open `Rindi-Agent-0.9.2.dmg` and drag **Rindi-Agent** onto **Applications**.
2. Open Rindi-Agent from your Applications folder. macOS asks once whether to open an app downloaded from the internet; choose **Open**.
3. In **Set up a model**, choose **Download** on the model that fits your Mac, or **Use Custom Folder…** if you already have it.
4. Choose **File › Open Workspace** (⌘O), pick a project folder, and describe what you want done.

The [User Guide](docs/USER-GUIDE.md) walks through everything else, with screenshots: sessions, approvals, the side panels, Computer Use, settings and troubleshooting. It's also on the [wiki](https://github.com/True2456/Rindi-Agent-releases/wiki), one page per topic.

## What it can do

- **Work on your code.** Reads, searches, edits and patches files in the workspace, and runs commands in a sandbox. In the default **Approve** mode, every change and command waits for you.
- **Use your Mac's apps.** Computer Use lets the agent read and operate native apps through Accessibility, in the background, without moving your cursor or taking focus. You watch it in a small picture-in-picture window.
- **Keep you in the loop.** Source control with staging, commits and branches; a file browser; long-running processes with live logs; a built-in web browser; and a task board where the agent can hand cards to worker agents.
- **Extend it.** Global instructions, reusable skills, and Model Context Protocol (MCP) servers.
- **Talk to it.** Dictate prompts instead of typing, and have replies read aloud with Apple's natural voices, including your own Personal Voice. Replies can also be saved as audio files.

## Benchmarks

**Intelligence.** On the [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/leaderboards/models), Qwen 3.8 Flash Next scores **40**, between Gemini 3.8 Flash (41) and DeepSeek V4.1 Flash (39). Qwen 3.8 27B scores **34** with thinking set to XHigh. These scores are for the full-precision models; see [Benchmarks](BENCHMARKS.md#intelligence) for the comparison and caveats.

**Speed.** Qwen 3.8 Flash Next on a MacBook Pro with an M5 Max and 128 GB, measured over a real 40-turn agent session:

| Context | Prompt processing | Reply (decode) |
| --- | ---: | ---: |
| 0–30k tokens | 1,120 tok/s | 66 tok/s |
| 30–90k tokens | 1,269–1,404 tok/s | 72–83 tok/s |
| 90–150k tokens | 1,072–1,211 tok/s | 77–78 tok/s |
| 150–180k tokens | 1,089 tok/s | 74 tok/s |

When the agent read a 15,000-token file into a conversation that was already 155,000 tokens long, its reply started 14 seconds later. [Benchmarks](BENCHMARKS.md) has the method, every context range, and the per-turn data.

## Privacy

Rindi-Agent uses the network only to:

- download models from huggingface.co,
- search the web and read pages, when the agent uses its web tools,
- reach MCP servers you add yourself,
- check for updates once a day on this page's update feed (you can turn this off in **Settings › About**),
- recognise dictation through Apple's online speech service, only for languages macOS can't recognise on the Mac.

Everything else, including inference, happens on your Mac.

## Updating

Rindi-Agent 0.9.1 and later check for updates once a day. When one is available, a window shows what's new, and **Install Update** downloads it, checks its signature and relaunches into the new version. To check yourself, choose **Rindi-Agent › Check for Updates…**. Your settings, chats, models and macOS permissions are kept.

**If you have 0.9.0**, which can't update itself, download the latest version once from this page and replace the app in Applications.

## Reporting problems

Open an issue in this repository with:

- what you did and what happened,
- your Mac model, memory and macOS version,
- the runtime log: **Settings › About › Runtime log › Reveal**, or `~/Library/Logs/Rindi-Agent/runtime.log`.

Check the log for anything private before you attach it: it can include file names from your projects.
