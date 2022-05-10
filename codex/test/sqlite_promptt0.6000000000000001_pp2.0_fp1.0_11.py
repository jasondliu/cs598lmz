import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect when multiple threads are running
#
# This test is a bit tricky because it creates two threads that each
# call sqlite3.connect concurrently. This is not something that normally
# happens, but it has been known to cause segfaults in the past.

# The test also tries to provoke a segfault by changing the library path
# while the second thread is running.

# The test will pass if the process does not crash.

# This is a reduced test case for http://www.sqlite.org/src/info/b5bc8b621b

