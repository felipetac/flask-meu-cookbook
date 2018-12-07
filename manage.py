'''Gerenciador da aplicação'''
from flask_script import Manager

from app import APP

MANAGER = Manager(APP)

if __name__ == '__main__':
    MANAGER.run()
