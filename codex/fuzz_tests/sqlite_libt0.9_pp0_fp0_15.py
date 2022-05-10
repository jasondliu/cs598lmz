import ctypes
import ctypes.util
import threading
import sqlite3
import re
import shutil
import logging
import StringIO
import os
import json
import unicodedata
import inspect

from waflib import Options, Configure

assert False, "Do not import this directly"

# NOTE: public headers must be installed, import them directly
import nkf
import Python.CtypesNKFEncodingBinding
# from nkf import*

def makeLibName(*libnames):
    for libname in libnames:
        ret = ctypes.util.find_library(libname)
        if None != ret:
            return ret
    return None

def callback(result, func, args):
    if result is None:
        return
    try:
        func(*args)
    except Exception:
        return

def makeCallLater( func, *args ):
    return threading.Timer( 0, callback, args = (None, func, args) )

class Singleton(type):
    def __init__(cls, name, bases, dct):
        super(Singleton, cls).__init__(name, bases
