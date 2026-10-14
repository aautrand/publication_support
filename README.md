# publications_support

Animated explainers for my videos about how I build software, made with
[Manim Community](https://www.manim.community/).

## Setup

Needs [uv](https://docs.astral.sh/uv/), plus Manim's system libraries
(`brew install cairo pango ffmpeg`) and a LaTeX install (MacTeX) for `MathTex`.

```sh
make install   # create .venv and install manim
make hooks     # enable the pre-push secret scan (needs gitleaks)
```

## Rendering

```sh
make preview SCENE=scenes/example_push_mirror.py           # draft, opens when done
make final   SCENE=scenes/example_push_mirror.py NAME=PushMirror   # 1080p60
```

Renders land in `media/videos/`, which is not tracked.

## Layout

- `scenes/` holds one file per video or topic. Each `Scene` subclass is one clip.
- `scenes/common/style.py` holds the shared colours, fonts and building blocks
  so every episode looks the same.

## Publishing

This repository is mirrored publicly on every push. `.githooks/pre-push`
blocks a push whose commits contain a secret (via
[gitleaks](https://github.com/gitleaks/gitleaks)) or a private network detail,
and the CI `secrets` job is the backstop.
