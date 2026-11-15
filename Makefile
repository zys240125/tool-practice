.PHONY: test lint format

test:
	uv run python -m pytest

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff format .