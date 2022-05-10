import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory') vs connection=sqlite3.connect(':memory'?
import multiprocessing
import os
import os.path
import sys
import re
import functools
import subprocess
import pycparser
import shutil
import datetime
import cProfile, pstats
import traceback
import time

from . import shell
from . import logging_util

import perun.collect.libc as libc

__author__ = "Tomas Kral"

# Decorators for profiling functions

def timing(f):
    @functools.wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
