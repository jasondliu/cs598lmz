import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import re
import json
import urllib.request
import urllib.parse

from queue import Queue

import argparse

from http.server import HTTPServer, BaseHTTPRequestHandler

# This is the path to the libspotify library
libspotify = ctypes.CDLL(ctypes.util.find_library('spotify'))

# These are the types we need to use for the function prototypes
c_int = ctypes.c_int
c_char_p = ctypes.c_char_p
c_void_p = ctypes.c_void_p
c_size_t = ctypes.c_size_t

# These are the functions we need to call
libspotify.sp_session_create.restype = c_int
libspotify.sp_session_create.argtypes = [c_void_p, c_void_p]

libspotify.sp_session_login.restype = c_int
