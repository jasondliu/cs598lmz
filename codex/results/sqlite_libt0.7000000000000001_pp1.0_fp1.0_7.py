import ctypes
import ctypes.util
import threading
import sqlite3
import os
import platform
import sys

from . import _sqlite3

class Error(Exception):
    pass

def _enable_shared_cache(enable):
    """
    Enable/disable shared cache
    """
    _sqlite3.enable_shared_cache(enable)

def _is_shared_cache_enabled():
    """
    Check if shared cache is enabled
    """
    return _sqlite3.is_shared_cache_enabled()

def _set_config_option(option, value):
    """Set the configuration option
    """
    rc = _sqlite3.sqlite3_config(option, value)
    if rc != _sqlite3.SQLITE_OK:
        raise Error("Error setting sqlite3 option")

def _set_thread_safety_level(level):
    """Set the thread safety level
    """
    _set_config_option(_sqlite3.SQLITE_CONFIG_MULTITHREAD)

def _set_synchronous_mode(mode):
    """Set the synchronous mode
    """

