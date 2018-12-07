'''Configurações da aplicação'''
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''Classe de configuração geral'''
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
    '''Classe de configuração em modo de desenvolvimento'''
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    '''Classe de configuração em modo de teste'''
    TESTING = True

class ProductionConfig(Config):
    '''Classe de configuração em modo de produção'''
    DEVELOPMENT = False
    DEBUG = False

CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
