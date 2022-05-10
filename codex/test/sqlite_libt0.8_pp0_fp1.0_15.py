import ctypes
import ctypes.util
import threading
import sqlite3
import os

BaseName = 'libvmod-querystring'

# list of available functions, with argument types
