import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

def connect(database=None, timeout=None):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    return True

# Declare global variables

current_thread = threading.current_thread()
print('Main thread: {}'.format(current_thread.name))

# Create threads

# Thread 1 connects to the database
thread1 = threading.Thread(name='database_thread', target=connect)
if thread1.daemon != True:
    thread1.daemon = True

# Thread 2 performs a search operation
thread2 = threading.Thread(name='search_thread', target=connect)
if thread2.daemon != True:
    thread2.daemon = True

# Thread 3 performs a write operation
thread3 = threading.Thread(name='write_thread', target=connect)
if thread3.daemon != True:
    thread3.daemon = True

# Execute threads

thread1.start()
thread2.start()
thread3.start()

