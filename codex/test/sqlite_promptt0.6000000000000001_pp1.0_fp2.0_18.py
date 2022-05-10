import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
db = sqlite3.connect("database/test.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
cursor.execute("INSERT INTO user(name, password) VALUES(?, ?)", ("test", "test"))
cursor.execute("SELECT * FROM user")
print(cursor.fetchall())
db.commit()
db.close()

# Test ctypes.util.find_library
print(ctypes.util.find_library("c"))
print(ctypes.util.find_library("m"))

# Test ctypes.CDLL
libc = ctypes.CDLL("libc.so.6")
print(libc.getpid())

# Test threading
def test_thread(i):
    print("I am thread %d" % i)
for i in range(5):
    t = threading.Thread(target=test_thread, args=(i,))
    t.start()
