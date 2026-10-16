# Benchmarks

How capable the models are, and how fast Rindi-Agent runs them during a real agent session. All inference runs on the Mac.

## Intelligence

Scores from the [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/leaderboards/models) (v4.3.2, October 2026), which combines ten evaluations: AA-Briefcase, GDPval-AA, AutomationBench-AA, Terminal-Bench 4.0, SciCode, Humanity's Last Exam, GDP.pdf, CritPt, AA-Omniscience and AA-LCR. The models Rindi-Agent runs are in bold; the others are hosted models for comparison.

| Model | Runs | Intelligence Index |
| --- | --- | ---: |
| Claude Opus 5.5 (max with fallback) | Cloud | 58 |
| Claude Haiku 5.5 (max) | Cloud | 43 |
| Gemini 3.8 Flash (high) | Cloud | 41 |
| **[Qwen 3.8 Flash Next](https://artificialanalysis.ai/models/qwen3-8-flash-next)** | **On your Mac** | **40** |
| DeepSeek V4.1 Flash (max) | Cloud | 39 |
| GPT-6 Luna (max) | Cloud | 38 |
| **[Qwen 3.8 27B](https://artificialanalysis.ai/models/qwen3-8-27b), thinking XHigh** | **On your Mac** | **34** |
| **Qwen 3.8 27B, thinking Medium** | **On your Mac** | **28** |
| **Qwen 3.8 27B, thinking Low** | **On your Mac** | **26** |

- **These are the full-precision models**, as served by their providers. Rindi-Agent runs 4-bit (Flash Next) and AWQ (27B) builds to fit in a Mac's memory, which can score a little lower. The local builds haven't been run through the index.
- **The 27B's score depends on how long it thinks.** Rindi-Agent's **Thinking** setting has the same three levels, Low, Medium and XHigh, and the default is **Medium**. Choose **XHigh** in the composer (or Shift-Tab) for harder tasks.
- Scores change as Artificial Analysis updates the index and adds models; see [their leaderboard](https://artificialanalysis.ai/leaderboards/models) for the current list.

## Speed

### Qwen 3.8 Flash Next on an M5 Max (128 GB)

**Prompt processing stays above 1,000 tokens per second all the way to 180,000 tokens of context, and replies come out at a median 66–83 tokens per second up to 180k.**

| Context | Turns | Prompt processing (tok/s) | Decode, median (tok/s) |
| --- | ---: | ---: | ---: |
| 0–30k | 10 | 1,120 | 66.3 |
| 30–60k | 8 | 1,269 | 82.8 |
| 60–90k | 2 | 1,404 | 71.8 |
| 90–120k | 8 | 1,211 | 77.6 |
| 120–150k | 6 | 1,072 | 77.4 |
| 150–180k | 5 | 1,089 | 73.9 |
| 180–210k | 1 | 1,085 | 49.0 (one turn) |

What that means in practice, from the same run:

| At context | New tokens in the turn | Time to first token |
| ---: | ---: | ---: |
| 89k | 27,133 | 19.5 s |
| 153k | 17,183 | 15.4 s |
| 170k | 15,303 | 14.0 s |
| 136k | 9,494 | 7.9 s |

The whole session ran 40 turns, processed 182,886 new prompt tokens and generated 11,438 tokens in 410 seconds. Per-turn data: [benchmarks/2026-10-16-flash-next-long-context.csv](benchmarks/2026-10-16-flash-next-long-context.csv).

#### The test

The agent is asked to read every Swift file of a ~180k-token inference engine codebase in full, one file per tool call, and then write an architecture overview. Every turn adds a file to the conversation, so the context grows from 8k to 180k tokens. The work is the same as a real coding session: many short tool-call turns on top of a long, cached conversation, with an occasional large file.

| | |
| --- | --- |
| Machine | MacBook Pro, Apple M5 Max (18-core CPU), 128 GB, macOS 27.2 |
| App | Rindi-Agent 0.9.1 engine (Rindi-NativeMLX `5e26c81`), default settings |
| Model | [Qwen 3.8 Flash Next MLX 4-bit](https://huggingface.co/True2456/Qwen3.8-Flash-Next-MLX-4bit) |
| Date | 16 October 2026 |

#### How to read the numbers

- **Prompt processing** is the new tokens in each turn divided by the time to the first reply token, totalled over the turns in the context range. The earlier part of the conversation comes from Rindi-Agent's cache and isn't counted again; that's why each turn only processes what it adds.
- **Decode** is the speed of the reply itself, including speculative decoding with the model's MTP drafter. Each range shows the median turn, because most turns are short tool calls whose speed depends on how predictable the next tokens are.
- **The first turn after loading is slower.** It processed 7,937 tokens at 759 tok/s while the weights were still being read into memory. That turn alone lowers the 0–30k figure; the other turns in that range with over 1,000 new tokens ran at 1,340–1,580 tok/s. Very short turns are slower per token because of fixed per-turn overhead.
- **Other apps matter.** This run had a music app open in the background. A second run on the same build, with two audio apps and a busy browser tab, was 17–31% slower throughout. Expect around 10% difference between runs even on a quiet Mac.

#### Your own numbers

Each reply in Rindi-Agent ends with a line like *1.8 s to first token · 8k cached · Decode 55.5 tok/s · 64% drafts*. **Settings › Logs** shows the same figures for every turn.

### Qwen 3.8 27B

Not yet measured for the published builds. This page will be updated.
