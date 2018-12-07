'''Bootstrap da aplicação'''
import os

from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from config import CONFIG

# Carrega variáveis de ambiente setadas no .env (comentar quando em produção)
load_dotenv()

# Define the WSGI application object
APP = Flask(__name__)

# Configurations
#app.config.from_object('config')
APP.config.from_object(CONFIG.get(os.environ["APP_SETTINGS"] or "default"))

# Sample HTTP error handling
@APP.errorhandler(404)
def not_found(exception): # pylint: disable=W0613
    '''Função padrão de exceção 404'''
    return jsonify({"result": "Url não encontrada..."}), 404
