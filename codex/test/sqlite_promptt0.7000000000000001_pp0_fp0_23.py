import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:", check_same_thread=False)
import logging
import sys
import os
import re
import subprocess
import fcntl

def _load_library(name):
    if sys.platform == "win32":
        return ctypes.cdll.LoadLibrary(name + ".dll")

    return ctypes.cdll.LoadLibrary(ctypes.util.find_library(name))

_lib = _load_library("pulse-simple")

class PulseError(Exception):
    pass

PA_CONTEXT_UNCONNECTED, PA_CONTEXT_CONNECTING, PA_CONTEXT_AUTHORIZING, PA_CONTEXT_SETTING_NAME, PA_CONTEXT_READY, PA_CONTEXT_FAILED, PA_CONTEXT_TERMINATED = range(7)

PA_CONTEXT_IS_GOOD = 0x0002
PA_CONTEXT_ERR_COMMAND = 0x0100
PA_CONTEXT_ERR_AUTHKEY = 0x0200
PA_CONTEXT_ERR_NOENTITY = 0
