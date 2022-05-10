import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:').execute('CREATE TABLE t(x)').execute('CREATE TABLE IF NOT EXISTS t(x)').fetchall()
import base64
import os
import os.path
import sys
import urlparse
import re

class CommandException(Exception):
    def __init__(self, command, code, message):
        Exception.__init__(self)
        self.command = command
        self.code = code
        self.message = message
        self.error = True

class Command(object):
    """
    This class represents a command in the mplayer process.

    """
    def __init__(self, name, **kwargs):
        self.name = name
        self.args = kwargs
        self.callbacks = []
        
