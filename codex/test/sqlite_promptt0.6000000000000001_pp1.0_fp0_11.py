import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

# Load libc
libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.malloc.restype = ctypes.c_void_p

# Global lock to prevent other threads from running
lock = threading.Lock()

# Thread function
def thread_function():
    # Lock the thread
    lock.acquire()
    # Connect to the database
    sqlite3.connect('test.db')
    # Unlock the thread
    lock.release()

# Create the threads
threads = []
for i in range(0, 100):
    threads.append(threading.Thread(target=thread_function))

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
