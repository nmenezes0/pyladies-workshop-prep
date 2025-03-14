.PHONY: check-python-code
check-python-code: ## Check Python code - linting and mypy
	uv run ruff check --select I .
	uv run ruff check .
	uv run mypy . --ignore-missing-imports

.PHONY: format-python-code
format-python-code: ## Format Python code including sorting imports
	uv run ruff check --select I . --fix
	uv run ruff check . --fix
	uv run ruff format .