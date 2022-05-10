import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect on a thread without the GIL
if sqlite3.sqlite_version_info >= (3, 7, 4):
    from test import test_support
    from test.test_support import captured_stdout
    import time

# ########################################################
# This is a test module for sqlite3. It defines test cases that
# exercise the sqlite3 C API. This allows some tests to be run
# without the Python interpreter.
#
# To run this test without the Python interpreter:
#
#     $ make sqlite3tester
#     $ ./sqlite3tester
#
# To run this test with the Python interpreter:
#
#     $ python sqlite3tester.py
#
# See also: sqlite3.h
#
# ########################################################


def setup():
    sqlite3.enable_callback_tracebacks(True)


def setup_module():
    try:
        os.unlink('test.db')
    except:
        pass

if sqlite3.sqlite_version_info >= (3, 7, 4):

