import select
import socket
import sys
import threading
import time
import traceback
import unittest
import weakref

from test import support
from test.support import _2G, _4G, _4G_PLUS_1, bigmemtest, cpython_only, import_module
from test.support.script_helper import assert_python_ok

# Skip these tests if there is no thread support.
threading = import_module('threading')
threading_setup = import_module('threading_setup')

# Skip these tests if the _thread module does not exist.
_thread = import_module('_thread')

#
# Test the thread module
#

def _wait_for_threads(threads):
    for t in threads:
        if t.isAlive():
            t.join()

def test_various_ops():
    # Try some thread operations -- fork a thread, and do various
    # operations from the main thread.
    mutex = threading.Lock()
    mutex.acquire()
    x = 0
    x
