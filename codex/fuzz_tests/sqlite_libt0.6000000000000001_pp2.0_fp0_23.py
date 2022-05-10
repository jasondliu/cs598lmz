import ctypes
import ctypes.util
import threading
import sqlite3

from a2.util.a2json import JsonObject, JsonEncoder
from a2.util.a2uri import A2Uri
from a2.util.a2time import A2_TIME_FORMAT

from a2.core.errors import *

LIB_A2CLOUD = ctypes.CDLL(ctypes.util.find_library("a2cloud"))

class A2Cloud(object):

    class __Cloud(object):
        def __init__(self):
            self.__lock = threading.RLock()
            self.__db = sqlite3.connect("a2cloud.db")
            self.__db.execute("""CREATE TABLE IF NOT EXISTS a2cloud (
                uri TEXT PRIMARY KEY,
                name TEXT,
                description TEXT,
                version TEXT,
                last_modified TEXT,
                icon TEXT,
                url TEXT,
                url_name TEXT,
                enabled BOOLEAN,
                installed BOOLEAN,
                installed_version TEXT,
                installed_last_modified TEXT
               
