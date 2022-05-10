import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
sqlite3.connect(":memory:")
# Test os.fork()
os.fork()
# Test os.forkpty()
# os.forkpty()
# Test fork() inside a thread
def thread_func():
    os.fork()

threading.Thread(target=thread_func).start()
# Test ctypes
ctypes.util.find_library("c")
# Test _multiprocessing
from _multiprocessing import SemLock
# Test faulthandler
import faulthandler
import io
faulthandler.dump_traceback(file=io.StringIO(), all_threads=False)
faulthandler.dump_traceback(file=io.StringIO(), all_threads=True)
# Test posix
import posix
import posix.fork
import posix.forkpty
import posix.forklock
import posix.forklock.forklock
import posix.forklock.forklock.forklock
