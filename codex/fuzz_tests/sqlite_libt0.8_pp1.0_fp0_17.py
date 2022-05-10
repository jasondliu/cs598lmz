import ctypes
import ctypes.util
import threading
import sqlite3
import argparse
import logging
import os
import sys
import re
import subprocess
import collections
import inspect
import shutil
import tempfile

logger = logging.getLogger(__name__)

def dbpath(path):
    if path == ':memory:': return path
    if path.startswith('~'): path = os.path.expanduser(path)
    return os.path.abspath(path)


def find_symbol(symbol):
    # do this in a subprocess because it may raise a fatal error (can't find
    # a symbol) and we don't want to blow up the main process.
    #
    # see https://github.com/leahneukirchen/elftools/blob/master/elftools/common/exceptions.py

    try:
        return subprocess.check_output(
            ['nm', '-C', '-D', '--dynamic', '--defined-only', symbol],
            close_fds=True).splitlines()[0].split()[0]

