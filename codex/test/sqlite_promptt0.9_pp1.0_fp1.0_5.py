import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() being called after fork()
lock = threading.Lock()

def child_code():
    db = sqlite3.connect(":memory:")

def fork_test():
    ret = ctypes.pythonapi.PyEval_SaveThread()
    for i in range(100000):
        pid = os.fork()
        if pid == 0:
            ctypes.pythonapi.PyEval_RestoreThread(ret)
            child_code()
            os._exit(0)
        else:
            os.waitpid(pid, 0)
            ctypes.pythonapi.PyEval_RestoreThread(ret)

lock.acquire()
print("Test one: don't fork while holding a lock acquired in the main thread")
pid = os.fork()
if pid == 0:
    lock.release()
    os.write(1, b"Unexpected")
    os._exit(1)
else:
    status = os.waitpid(pid, 0)[1]
