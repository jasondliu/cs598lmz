import codecs
codecs.register(search_function)

# import global variables
from config import (
    DATABASE_PASSWORD,
    DATABASE_USER,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_DB,
    DATABASE_CHARSET,
    DATABASE_COLLATE,
    SESSION_COOKIE_NAME,
    SESSION_COOKIE_HTTPONLY,
    SESSION_COOKIE_SECURE,
    SESSION_EXPIRE_AT_BROWSER_CLOSE,
    PERMANENT_SESSION_LIFETIME,
    SECRET_KEY
)
# import custom functions
from utils import project_path_join

# define configs of application

project_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

# application configs
class BaseConfig(object):
    # cookie configs
    SESSION_COOKIE_NAME = SESSION_COOK
