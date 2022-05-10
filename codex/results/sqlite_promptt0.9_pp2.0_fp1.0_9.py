import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(None, uri=True)

wPDB = ctypes.CDLL(ctypes.util.find_library('WebPracticalDB'))
libc = ctypes.CDLL(ctypes.util.find_library('c'))

start_time = libc.time(None)

class Updater:
    def update_lib(self, value: bytes):
        print(value)


updater = Updater()

me = threading.currentThread()

updater.update_lib(b"Start")

def connect_db(updater):
    conn2 = sqlite3.connect('wPDB://updater? type=code&code=' + str(id(updater)))
    # conn = sqlite3.connect(None, uri=True)
    # connect_db()
    wPDB.update_updater(id(updater))
    c = conn2.cursor()
    num_rows = 0
    for row in c.execute("SELECT * FROM Stuff"):
        num_rows
