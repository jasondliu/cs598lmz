import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")


class sqlite3_threading_test(threading.Thread):

    def __init__(self, db_name):
        threading.Thread.__init__(self)
        self.db_name = db_name

    def run(self):
        db = sqlite3.connect(self.db_name)
        db.close()
        print("SQLite connection completed!")


def main():
    db_name = ""
    num_threads = 10000
    threads = []

    if (len(sys.argv) < 2):
        print("Usage: %s <sqlite3_db_name>" % (sys.argv[0]))
        sys.exit(1)

    db_name = sys.argv[1]

    # Start threads
    for i in range(num_threads):
        t = sqlite3_threading_test(db_name)
        threads.append(t)
        t.start()

    # Wait for threads to complete
