import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("wpdtest.db", uri=True)

#test https://pysqlite.readthedocs.io/en/latest/sqlite3.html

import _ctypes
_ctypes.PyDLL("/usr/lib/libsqlite3.so.0")
libc = ctypes.CDLL("/usr/lib/libicui18n.so.48", use_errno=True) #https://gist.github.com/lagopus/16270d7f94e48f18e0ff75c6653ed5e5
libc.u_errorName.restype = ctypes.c_char_p

import socket
import os

try:
    import BaseHTTPServer
    _BaseHTTPServer = BaseHTTPServer
except BaseException:
    import http.server
    _BaseHTTPServer = http.server

import urllib
try:
    import fcntl
except BaseException:
    fcntl = None

