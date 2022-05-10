import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import re
import pwd
import grp
import logging
import hashlib
import time
import datetime
import json
import fcntl
import shutil

from . import utils

# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_directory(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory)

def check_file(file):
    if not os.path.isfile(file):
        open(file, 'a').close()

def get_db_path(dirname):
    return os.path.join(dirname, 'db.sqlite3')

def get_mtime(path):
    stat = os.stat(path)
    return datetime.datetime.fromtimestamp(stat.st_mtime)

def get_ctime(path):
    stat = os.stat(path)
    return datetime.datetime.fromtimestamp(stat.st_ctime)
