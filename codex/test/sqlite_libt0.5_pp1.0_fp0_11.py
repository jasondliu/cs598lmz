import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os

from . import wrapper
from . import utils
from . import config
from . import database

class Language:
    def __init__(self, code):
        self.code = code
        self.name = None
        self.translate = None
        self.translate_reverse = None
        self.translate_regex = None
        self.translate_regex_reverse = None

class Core:
    def __init__(self):
        self.__lib = None
        self.__db = None
        self.__lib_version = None
        self.__languages = {}
        self.__languages_lock = threading.Lock()
        self.__lib_path = None
        self.__lib_path_lock = threading.Lock()
        self.__db_path = None
        self.__db_path_lock = threading.Lock()
        self.__initialized = False
        self.__initialized_lock = threading.Lock()
        self.__config = None
