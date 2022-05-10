import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared")

# This is the only function that is needed to be exposed to the outside.
# It is called by the main thread to start the worker thread.
def start_worker_thread(db_file):
    global worker_thread
    worker_thread = WorkerThread(db_file)
    worker_thread.start()

# This is the only function that is needed to be exposed to the outside.
# It is called by the main thread to stop the worker thread.
def stop_worker_thread():
    global worker_thread
    worker_thread.stop()

# This is the only function that is needed to be exposed to the outside.
# It is called by the main thread to get the results from the worker thread.
def get_results():
    global worker_thread
    return worker_thread.get_results()

class WorkerThread(threading.Thread):
    def __init__(self, db_file):
        threading.Thread.__init__(self)
        self.db_file = db_file
