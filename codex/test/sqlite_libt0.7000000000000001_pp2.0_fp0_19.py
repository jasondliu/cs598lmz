import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import errno
import sys
import random
import mmap

try:
    from .utils import singleton
except (ImportError, ValueError):
    from utils import singleton

DB_VERSION = '1.0'
DB_NAME = 'pyrasite.db'

RASITE_LIB_PATH = os.path.join(os.path.dirname(__file__), 'rasite.so')

DEFAULT_TLS_THRESHOLD = 1
DEFAULT_TLS_SAMPLE_RATE = 100


def create_db_tables(connection):
    c = connection.cursor()

    c.execute("""
    CREATE TABLE frames (
        process TEXT,
        pid INTEGER,
        thread INTEGER,
        address TEXT,
        lib TEXT,
        symbol TEXT,
        offset INTEGER,
        samples INTEGER,
        percent REAL
    )
    """)

