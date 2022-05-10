import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import os
import sys
import time
import random
import string
import tempfile
import shutil
import subprocess

import pytest

from . import _util
from . import _sqlite


# ------------------------------------------------------------------------------
# --- Tests
# ------------------------------------------------------------------------------

class Test_sqlite3_connect_uri:

    def test_connect_uri_memory(self, sqlite3_connect):
        con = sqlite3_connect(':memory:')
        assert con.execute('PRAGMA database_list').fetchall() == [(0, 'main', ':memory:')]

    def test_connect_uri_memory_cache_shared(self, sqlite3_connect):
        con = sqlite3_connect('file:memory:?cache=shared', uri=True)
        assert con.execute('PRAGMA database_list').fetchall() == [(0, 'main', ':memory:')]

    def test_connect_uri_memory_cache_private(self, sqlite3_connect):
       
