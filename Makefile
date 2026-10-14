SHELL := /bin/bash

# Usage: make preview SCENE=scenes/example_push_mirror.py [NAME=PushMirror]
SCENE ?= scenes/example_push_mirror.py
NAME ?=

install:
	uv sync

# Fast low-quality render that opens when done.
preview:
	uv run manim -p $(SCENE) $(NAME)

# 1080p60 render for the final edit.
final:
	uv run manim -qh $(SCENE) $(NAME)

# 4K render, for zooming in during editing.
final-4k:
	uv run manim -qk $(SCENE) $(NAME)

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff check --fix .
	uv run ruff format .

clean:
	rm -rf media/

# Turn on the pre-push secret scan in .githooks/ (needs gitleaks).
hooks:
	git config core.hooksPath .githooks

.PHONY: install preview final final-4k lint format clean hooks
