import ctypes
import ctypes.util
import threading
import sqlite3
import os

from datetime import datetime, timedelta

import logging
_logger = logging.getLogger('collectd')

class Plugin(object):
    def __init__(self, name, types, type_instance, instance, write_callback_pointer, identifier=None, host='localhost'):
        self.name = name
        self.types = types
        self.type_instance = type_instance
        self.instance = instance
        self.id = identifier
        self.host = host
        self.write_callback = write_callback_pointer.value

    def dispatch(self, values):
        c_host = ctypes.create_string_buffer(self.host)
        c_plugin = ctypes.create_string_buffer(self.name)
        c_type = ctypes.create_string_buffer(self.types)
        c_type_instance = ctypes.create_string_buffer(self.type_instance)
        c_instance = ctypes.create_string_buffer(self.instance)

        c_identifier = ctypes.c_uint
