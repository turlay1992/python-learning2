# Actions for new app:
uv python install 3.13
# Встанови менеджер версій:

uv python pin 3.13
# Запінити її на Python 3.13

uv init --package  
# --package - Created with tree structure (not flat). tree - Захист від "випадкового" імпорту

uv add httpx
uv add --dev pytest 
# adding some dependencies

uv sync

uv run python -c "import httpx; print(httpx.__version__)"

uv run python -c "import python_learning2; python_learning2.main()"
# має вивести те саме повідомлення main.py

uv run 

# ==============================

# ==== Ruff ==== 
uv add --dev ruff

і в pyproject.toml — секції:

[tool.ruff]
line-length = 100
target-version = "py313"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "SIM", "S"]

uv run ruff check .
uv run ruff check . --fix

# ---------------------------

uv run ruff format .
# застосовує зміни.

uv run ruff format --check .
# нічого не змінює, тільки перевіряє й повертає код виходу 1/0

uv run ruff format --diff .
# показує, що б змінилось, без застосування

і в pyproject.toml — секції:
[tool.ruff.format]
quote-style = "double"

# ==== Mypy ==== 

uv add --dev mypy

і в pyproject.toml — секції:
[tool.mypy]
python_version = "3.13"
strict = true
disallow_untyped_defs = true
warn_unused_ignores = true
warn_return_any = true

uv run mypy src/

# ==== pip-audit ==== 

uv add --dev pip-audit
uv run pip-audit

# ==== pre-commit hooks ==== 
uv add --dev pre-commit

need to manually create .pre-commit-config.yaml with hooks

uv run pre-commit install        # ставить реальний хук у .git/hooks/pre-commit
uv run pre-commit run --all-files   # прогнати одразу на всіх файлах, а не тільки на staged

Створи .vscode/settings.json з контентом:
   {
     "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
     "editor.formatOnSave": true,
     "[python]": {
       "editor.defaultFormatter": "charliermarsh.ruff",
       "editor.codeActionsOnSave": {
         "source.fixAll.ruff": "explicit",
         "source.organizeImports.ruff": "explicit"
       }
     }
   }

# ==== VSCode Extensions ==== 
Python
Pylance
Ruff

# ==== Logging ====

import logging
logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

 $env:LOG_LEVEL="DEBUG"; uv run python -m python_learning2.cloude_tasks.class_methods

# ==== Tests ====

Папка tests/ 
uv run pytest

і в pyproject.toml — секції:
[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["S101"]

# File run ex.

uv run python -m python_learning2.cloude_tasks.class_methods 

# ==== 


uv init 
# створює скелет проєкту. Команда генерує pyproject.toml, базовий пакет (з src/-layout або плаский, залежно від флагів), і якщо в директорії вже є .git/.python-version — підхоплює їх, а не перезатирає.

# uv add/uv sync/uv lock — це і є дисципліна лок-файлу

uv add httpx 
# дописує залежність у [project.dependencies] файлу pyproject.toml і одразу оновлює uv.lock. 

uv add --dev pytest 
# робить те саме, але в групу дев-залежностей. 

uv sync 
# встановлює віртуальне середовище (.venv) так, щоб воно точно відповідало лок-файлу — не "приблизно та версія", а рівно та, аж до кожної транзитивної залежності. 

uv lock 
# перегенерує лок-файл із поточних обмежень у pyproject.toml, не торкаючись самого середовища. 

uv run 
# команда виконує команду всередині проєктного середовища без ручної активації — це прибирає цілий клас багів типу "забув activate venv, і запустилось не тим Python".
