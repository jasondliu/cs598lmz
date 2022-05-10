import gc, weakref
import sqlite3
import string, logging, warnings
import sys, os, glob, shutil, tempfile
import collections, itertools

try:
    import thread
    import threading
    from threading import Lock, currentThread, Lock as _RLock
except ImportError:
    #  threading is only available in Python 2.4 or newer
    pass

import atexit
import copy_reg

# bw compat; cookbook suggests the following instead
#try:
#    from logging import NullHandler
#except ImportError:
#    class NullHandler(logging.Handler):
#        def emit(self, record):
#            pass


def _get_module(name):
    # start with core common modules
    if name in _modules:
        return name
    # check if this is a core module (optimized default path)
    if name.startswith("sqlalchemy.ext.compiler"):
        compmod = __import__("compiler", globals(), locals())
        if hasattr(compmod, "sql"):
            return "sqlalchemy
