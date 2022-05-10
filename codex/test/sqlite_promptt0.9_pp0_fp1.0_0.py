import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import datetime
# Test datetime
import collections
# Test collections
import os
import shutil
import sys
# Test sys
import pytz
import tzlocal
import decimal
import ipaddress
import logging


foreground_process_pid = os.getpid()

log = logging.getLogger("PY4CHAN")
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
if log_file:
    ch.stream = open(log_file, "a")
else:
    ch.stream = sys.stdout
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


