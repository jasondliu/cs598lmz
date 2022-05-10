import select
# Test select.select() with a readable and a writable pipe.
# This test is not comprehensive.
import unittest
import os
import sys
import errno
from test.support import TESTFN, run_unittest, import_module, unlink
try:
    import threading
except ImportError:
    threading = None
try:
    import resource
except ImportError:
    resource = None
try:
    import _thread
except ImportError:
    _thread = None
try:
    import _dummy_thread
except ImportError:
    _dummy_thread = None
try:
    import _multiprocessing
except ImportError:
    _multiprocessing = None
if _thread:
    import _thread as thread
elif _dummy_thread:
    import _dummy_thread as thread
else:
    thread = None
if threading:
    from threading import Thread as _Thread
else:
    _Thread = None
try:
    import signal
except ImportError:
    signal = None
if sys.platform == 'win32':
    import ms
