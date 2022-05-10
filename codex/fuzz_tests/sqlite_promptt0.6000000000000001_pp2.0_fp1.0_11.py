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

def test_threaded_connect(library_name):
    def thread_func():
        print "thread_func"
        db = sqlite3.connect(":memory:")
        db.close()

    try:
        lib = ctypes.CDLL(library_name)
    except:
        print "sqlite library not found"
        return

    old_path = lib.sqlite3_libversion()
    print "old_path:", old_path

    t = threading.Thread(target=thread_func
