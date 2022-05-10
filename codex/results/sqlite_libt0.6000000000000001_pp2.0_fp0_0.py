import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import time
import re
import sys
import os

if sys.platform == 'darwin':
    default_lib_path = '/usr/local/lib/libspotify.dylib'
else:
    default_lib_path = ctypes.util.find_library('spotify')

libspotify = ctypes.CDLL(default_lib_path)

# version.h
SPOTIFY_API_VERSION = libspotify.SPOTIFY_API_VERSION
SPOTIFY_API_VERSION_MAJOR = libspotify.SPOTIFY_API_VERSION_MAJOR
SPOTIFY_API_VERSION_MINOR = libspotify.SPOTIFY_API_VERSION_MINOR
SPOTIFY_API_VERSION_PATCH = libspotify.SPOTIFY_API_VERSION_PATCH

# error.h
SP_ERROR_OK = libspotify.SP_ERROR_OK
SP_ERROR_BAD_API_VERSION = libspotify.SP_ERROR_BAD_API_VERSION
SP_
