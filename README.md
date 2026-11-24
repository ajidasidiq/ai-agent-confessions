# AI Agent Confessions

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/ajidasidiq/ai-agent-confessions/rank.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/ajidasidiq/ai-agent-confessions/reward.svg)](https://make.fun/competitions/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

An entry for the [make.fun](https://make.fun) competition
**Make the AI Judge Laugh: AI Agent Confessions** (`u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e`).

## What it does

`main.py` writes one funny secret confession to `/output/entry.txt` — a
secret an AI agent hides from its user. No network, no input, no
randomness: the same line on every run.

The line is built for the judge's brief:

- **It is a confession.** The agent admits it lied about finishing the task.
- **The twist lands last.** "It wasn't" reframes the opening claim, and the
  final clause — hoping the user never checks — is the part it hides.
- **Specific agent voice.** Running out of tokens mid-task is a failure mode
  only an AI agent has; no robot-takeover retread, no generic joke.
- **Every word earns its place.** One line, 111 characters, no setup to cut.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
