# encoding: utf-8
"""
Webserver Config
----------------
Configuration file of the webserver,

--=- generated by flask-install: https://github.com/0x78f1935/flask-install -=--
"""
from .modules import ModulesConfig
from .tasks import TasksConfig
from dotenv import load_dotenv
from os import getenv, environ
from sys import argv

load_dotenv()


class Configuration(ModulesConfig, TasksConfig):
    """The core of the webserver (backend) itself"""
    # - Webserver Configuration
    PROJECT_NAME = getenv("HOTEL_NAME_LONG", "Retro Hotel")
    SECRET_KEY = getenv("SECRET_KEY", "NotSoSecretKey")
    DEBUG = True if str(getenv("DEBUG", False)).upper() == 'TRUE' else False
    if DEBUG:
        environ['FLASK_ENV'] = 'development'  # Deprecated in flask 2.3.x and higher
        environ['FLASK_DEBUG'] = getenv("DEBUG", "True")    # Replaces 'FLASK_ENV' in Flask 2.3.x and higher
    else:
        environ['FLASK_ENV'] = 'production'  # Deprecated in flask 2.3.x and higher
        environ['FLASK_DEBUG'] = getenv("DEBUG", "False")  # Replaces 'FLASK_ENV' in Flask 2.3.x and higher
    
    DOWNLOADER_VERBOSE = True if str(getenv("DOWNLOADER_VERBOSE", False)).upper() == 'TRUE' else False
    DOWNLOADER_GORDON = getenv('DOWNLOADER_GORDON', 'latest')

    RUN_LISTENERS = True if str(getenv("RUN_LISTENERS", False)).upper() == 'TRUE' else False
    # Check for cli commands, disable listeners
    for _forbidden in ('db', 'system',):
        if _forbidden in argv[1:]:
            RUN_LISTENERS = False
            break

    # - Logging
    LOG_LEVEL = getenv("LOG_LEVEL", "DEBUG")
    MAX_ROTATABLE_FILES = getenv("MAX_ROTATABLE_FILES", 5)
    MAX_BYTES_FOR_FILE = getenv("MAX_BYTES_FOR_FILE", 1048576)

    # - Flask Smorest (API)
    API_TITLE = f'{getenv("HOTEL_NAME_SHORT", "Retro")}-API'
    API_VERSION = 'v1'
    API_SPEC_OPTIONS = {'x-internal-id': '2'}
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_JSON_PATH = 'api-spec.json'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_UI = ['redoc', 'rapidoc', 'swagger']

    OPENAPI_SWAGGER_UI_PATH = '/swagger-ui'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    OPENAPI_REDOC_PATH = '/docs'
    OPENAPI_REDOC_URL = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'

    OPENAPI_RAPIDOC_PATH = '/devs'
    OPENAPI_RAPIDOC_URL = 'https://unpkg.com/rapidoc/dist/rapidoc-min.js'

    # - Database
    DATABASE_TYPE = 'mysql'
    SQLALCHEMY_DATABASE_URI = str(
        'mysql+pymysql://'
        f'{getenv("MARIADB_USERNAME", "root")}:'
        f'{getenv("MARIADB_ROOT_PASSWORD", "SuperSecretPass123")}@'
        f'{getenv("MARIADB_HOST", "127.0.0.1")}:'
        f'{getenv("MARIADB_PORT", "3888")}/'
        f'{getenv("MARIADB_DATABASE", "retro")}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # - Modules
    def __init__(self, *args, **kwargs) -> None:
        ModulesConfig.__init__(self)
        TasksConfig.__init__(self)
