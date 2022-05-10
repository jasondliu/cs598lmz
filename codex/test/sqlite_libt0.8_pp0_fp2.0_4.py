import ctypes
import ctypes.util
import threading
import sqlite3 as sqlite
import hashlib
import time
import datetime
import errno
import pkg_resources
import json
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def get_filename():
    return pkg_resources.resource_filename("zephyrus", "data/notifications.db")


def get_db_connection():
    return sqlite.connect(get_filename(), detect_types=sqlite.PARSE_DECLTYPES)


def get_table_names(db_connection):
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return db_cursor.fetchall()


def create_default_tables(db_connection):
    db_cursor = db_connection.cursor()
