import ctypes
import ctypes.util
import threading
import sqlite3
import time
import socket
import platform
import os

if platform.system() not in ['Darwin', 'Linux', 'Windows']:
    raise Exception('Unsupported platform')

BAD_FILE = 0xFFFFFFFF

def pydi_printf(fmt, *args):
    out = fmt % args
    if platform.system() == 'Windows':
        out += '\n'
    sys.stdout.write(out)
    sys.stdout.flush()

def set_file(path):
    # hash: fully qualified file name
    #       return bad file if file not found
    # value: a ',' separated list which maps
    #        to the indexes in the printf format string
    exe_type = platform.system()
    if exe_type == 'Darwin':
        format_fmt = '%s %s %s %s %s %s %s %s %s %s'
    elif exe_type == 'Windows':
        format_fmt = '%s %s %s %s %s %s %s %s %
