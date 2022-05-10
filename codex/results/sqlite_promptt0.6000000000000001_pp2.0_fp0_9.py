import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect works with uri
print(sqlite3.connect('file:memory:?mode=memory&cache=shared'))

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

# Get a handle to the main thread
main_thread = libc.pthread_self()

threads = []

for i in range(10):
    t = threading.Thread(target=lambda: None)
    t.start()
    threads.append(t)

# Assert that the main thread is not in the list
assert main_thread not in [libc.pthread_self() for t in threads]

# Wait for all threads to finish
for t in threads:
    t.join()
 
# Assert that the main thread is still the same
assert main_thread == libc.pthread_self()
