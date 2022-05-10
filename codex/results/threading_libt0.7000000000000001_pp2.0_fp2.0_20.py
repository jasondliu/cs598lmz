import threading
threading.stack_size(67108864) # 64MB stack

from datetime import datetime, timedelta
from decorator import decorator
from inspect import getfile, currentframe
from json import loads, dumps
from logging import getLogger, StreamHandler, FileHandler, DEBUG, INFO, WARNING, ERROR, CRITICAL, Formatter
from os import path, system
from random import randint, seed
from sys import stdout
from time import sleep, time
from traceback import format_exc
from urllib.request import urlopen, Request
from uuid import uuid4

@decorator
def try_except_log(function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except:
        getLogger('error').error(format_exc())

def get_config_data():
    return loads(urlopen('http://d3c33hcgiwev3.cloudfront.net/image/AOwfTpkxT7SI_1.json').read())

def get_authentication_data():
    config
