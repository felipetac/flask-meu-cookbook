# Felipe Flask Cookbook

## Preparação do Ambiente

```sh
pyenv shell <versão_python_ex_3.7.0>

mkdir <nome_do_projeto>

cd <path_nome_do_projeto>

git init

python -m venv <nome_virtual_env_ex_.venv>

source <path_venv>/bin/activate

pip install --upgrade pip

pip install pylint python-dotenv

touch .env .gitignore .python-version .pylintrc README.md config.py manage.py requirements.txt

mkdir app

cd app

touch __init__.py
```

Edite o arquivo _.python-version_:

```txt
<versão_python_ex_3.7.0>
```

Edite o arquivo _.gitignore_:

```txt
<path_do_virtual_env_ex_.venv>
__pycache__
```

## Configurações VSCode para o projeto

```sh
mkdir .vscode

cd .vscode

touch settings.json
```

Edite o arquivo _settings.json_:

```json
{
    "python.pythonPath": "${workspaceFolder}/.venv/bin/python",
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/*.pyc": {"when": "$(basename).py"},
        "**/__pycache__": true
    },
    "python.linting.enabled": true,  
}
```

## Instalando Flask

```sh
pip install Flask Flask-Script

pip freeze > requirements.txt
```

## Editando as Configurações

No arquivo _config.py_:

```python
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```
