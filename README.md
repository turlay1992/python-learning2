# Python Project: Creation and Deployment

A Python project template demonstrating reproducible project setup, development tooling, quality checks, testing, and application execution with `uv`.

## Prerequisites

Before cloning the repository, install:

* Git
* `uv` — use the project-compatible version specified by the team/environment.

The repository already contains a `.python-version` file. You **do not need to install Python manually**: `uv` will detect the required Python version and install/use it when setting up the project.

Verify `uv`:

```bash
uv --version
```

## Setup

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd <project-directory>
```

Synchronize the project environment:

```bash
uv sync
```

`uv sync` uses the existing `uv.lock` file to create/update `.venv` with the exact dependency versions defined by the lock file, including transitive dependencies.

No manual virtual-environment activation is required when using `uv run`.

## Running the App

The project provides an entry point through `[project.scripts]`. Run the application with:

```bash
uv run <project-command>
```

You can also run individual modules directly with Python's `-m` option:

```bash
uv run python -m <package>.<module>
```

For example:

```bash
uv run python -m python_learning2.cloude_tasks.class_methods
```

`uv run` executes commands inside the project's managed environment, ensuring that the correct Python interpreter and dependencies are used.

## Development Workflow

Run the following quality gates before committing changes.

### Ruff — linting

Check the code:

```bash
uv run ruff check .
```

Automatically apply available fixes:

```bash
uv run ruff check . --fix
```

### Ruff — formatting

Format the project:

```bash
uv run ruff format .
```

Check formatting without modifying files:

```bash
uv run ruff format --check .
```

Preview formatting changes:

```bash
uv run ruff format --diff .
```

### Mypy — static type checking

Run strict type checking:

```bash
uv run mypy src tests
```

### pip-audit — dependency security audit

Check project dependencies for known security vulnerabilities:

```bash
uv run pip-audit
```

### Pytest — tests

Run the test suite:

```bash
uv run pytest
```

### Quality-gate checklist

Before committing:

```text
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
uv run pip-audit
uv run pytest
```

## Pre-commit Hooks

The repository already contains the pre-commit configuration:

```text
.pre-commit-config.yaml
```

Nothing needs to be created manually.

Install the Git hooks:

```bash
uv run pre-commit install
```

Run all configured hooks against the entire repository:

```bash
uv run pre-commit run --all-files
```

After installation, the hooks will also run automatically against staged files during `git commit`.

## Editor Setup

The project contains a ready-to-use VS Code configuration:

```text
.vscode/settings.json
```

No manual configuration is required. Open the project directory in VS Code and the repository settings will be applied automatically.

Recommended extensions:

* **Python** — Microsoft
* **Pylance** — Microsoft
* **Ruff** — Ruff

The project is configured to use Ruff as the Python formatter and to apply Ruff code actions when explicitly requested.

## Logging

The application uses Python's standard `logging` module.

The logging level is controlled through the `LOG_LEVEL` environment variable. If the variable is not specified, the default level is `INFO`.

For example, in PowerShell:

```powershell
$env:LOG_LEVEL="DEBUG"
uv run python -m python_learning2.cloude_tasks.class_methods
```

This allows the logging verbosity to be changed without modifying the source code.
