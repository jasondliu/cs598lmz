import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/tmp/test.db") as conn:

class LibC:
    def __init__(self):
        self.libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

    def sched_yield(self):
        self.libc.sched_yield()


if __name__ == "__main__":
    libc = LibC()
    for _ in range(0, 5):
        print("Hello from the main thread")
        libc.sched_yield()

    def thread_func():
        for _ in range(0, 5):
            print("Hello from a thread")
            libc.sched_yield()

    thread = threading.Thread(target=thread_func)
    thread.start()
    thread.join()
    print ("done")
