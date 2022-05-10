import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os

import modules.bps

# For self-test purposes, allow the test suite to override the location of
# BPS.
if 'BPS_DIR' in os.environ:
    BPS_DIR = os.environ['BPS_DIR']
else:
    BPS_DIR = ctypes.util.find_library('bps')
if not BPS_DIR:
    raise RuntimeError('Could not locate BPS library')

# Use ctypes to load the BPS library and make it available to Python code.
BPS = ctypes.CDLL(BPS_DIR)

# Define a new exception class for BPS errors.
class BPSError(Exception): pass

def safe_call(fn, *args):
    """
    Call a BPS function, raise an exception if it fails.
    """
    ret = fn(*args)
    if ret != 0:
        raise BPSError('BPS function {} failed: {}'.format(fn.__name__, ret))

