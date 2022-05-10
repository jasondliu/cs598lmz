import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect for parent process.
SQLITE3_CONNECT_TEST = "sqlite3_connect"
SQLITE3_CONNECT_TEST_ERROR = "sqlite3_connect_error"
SQLITE3_CONNECT_TEST_RESULT = "sqlite3_connect_result"
# Test sqlite3.connect for child process.
SQLITE3_CONNECT_CHILD_TEST = "sqlite3_connect_child"
SQLITE3_CONNECT_CHILD_TEST_RESULT = "sqlite3_connect_child_result"
# Test sqlite3.connect in thread.
SQLITE3_CONNECT_THREAD_TEST = "sqlite3_connect_thread"
SQLITE3_CONNECT_THREAD_TEST_RESULT = "sqlite3_connect_thread_result"
# Test sqlite3.connect for a process that has already called sqlite3_initialize()
# (See issue #17 for more details).
SQLITE3_CONNECT_INITIALIZE_TEST = "sqlite3_connect_initialize"
SQLITE3
