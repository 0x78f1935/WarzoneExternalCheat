# encoding: utf-8
"""
Webserver Config
----------------
Configuration file of the webserver,

--=- generated by flask-install: https://github.com/0x78f1935/flask-install -=--
"""
from .modules import ModulesConfig


class Configuration(ModulesConfig):
    """The core of the webserver (backend) itself"""
    # - Webserver Configuration
    PROJECT_NAME = 'Retro'
    SECRET_KEY = 'YYonvLmC6jD14j5batJFEHIGImrINFHkl57EGW2ZobKXV9UsiW0pY-h-evk9O0XKeV5BC3dl1Nqxojq80_V6p0fknha3WtXql8T0QBH2_T6POv_Tdj2FEJwYU_WVVLu8kEedEFgkXeijLSdyFOecq-HxcI11MCPW99khWEbY8pA'  # noqa: B950

    # - Flask Smorest (API)
    API_TITLE = 'Retro-API'
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
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:admin@127.0.0.1:3306/flaskapp_schema'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # - Modules
    def __init__(self, *args, **kwargs) -> None:
        ModulesConfig.__init__(self)
