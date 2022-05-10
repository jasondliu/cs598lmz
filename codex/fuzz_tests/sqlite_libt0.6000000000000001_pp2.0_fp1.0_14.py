import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import glob

from . import const
from . import util
from . import config
from . import database

def _init():
    """
    Loads the libspotify library and returns a handle to the library.

    Returns a handle to the loaded libspotify library.
    """
    libspotify_so = ctypes.util.find_library('spotify')
    if not libspotify_so:
        raise RuntimeError("Could not find the libspotify shared library")
    libspotify = ctypes.CDLL(libspotify_so)
    return libspotify

def _check(error):
    """
    Checks the error code returned from a libspotify function and raises
    an exception if it is an error.

    Returns the value of the error code.
    """
    if error < 0:
        raise SpotifyError(error)
    return error

libspotify = _init()

def ffi(func):
    """
    Wraps a libspotify function, converting the arguments to and from
    python types.

    Returns the
