import ctypes
import ctypes.util
import threading
import sqlite3
import re

from helper.src.utils import *

kAPI = ctypes.util.find_library("ffi")
kVersion = "1"

class API(object):

    def __init__(self):
        self._api = ctypes.CDLL(kAPI, use_errno=True)
        self._api.ffi_init()

        status = ctypes.c_int()
        self._db = self._api.ffi_open_db(".", kVersion, ctypes.byref(status))
        check_exception(status.value)

        self._api.ffi_set_callbacks(self._api.ffi_get_metrics, self._api.ffi_get_event)
        self._api.ffi_set_database(self._db)

    def close(self):
        self._api.ffi_close_db(self._db)
        self._api.ffi_deinit()

class Server(object):

    def __init__(self):
        self._server_event = threading.Event
