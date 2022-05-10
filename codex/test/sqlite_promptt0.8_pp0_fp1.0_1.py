import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
from contextlib import contextmanager
import os
import io
import sys
import unittest
from unittest import mock
from test import support

# skip dbtest if no sqlite3 module, or it is too old
support.import_fresh_module('sqlite3')

# for spawn_python()
import subprocess
from subprocess import PIPE, STDOUT
import signal
import gc
import textwrap
import warnings
import tempfile
import shutil

from test.support import import_helper
locale_module = import_helper.import_fresh_module('locale')

SQLITE_OK = 0
SQLITE_ROW = 100
SQLITE_DONE = 101

# The default configuration setting for shared cache
cache = sqlite3.connect(':memory:', uri=True)
setting = cache.execute("PRAGMA cache_size").fetchone()[0]
cache.close()

# Before Python 3.6, this test uses a function to start a thread in order
#
