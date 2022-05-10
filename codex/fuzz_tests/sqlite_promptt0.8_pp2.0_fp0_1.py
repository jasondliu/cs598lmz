import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() as a context manager
with sqlite3.connect('test.db') as conn:
    conn.execute("create table person(firstname, lastname, age)")
    WHO = (("Joe", "Doe", 35),
           ("John", "Doe", 20),
           ("Jane", "Doe", 18),
           ("Jill", "Doe", 50))
    conn.executemany("insert into person(firstname, lastname, age) values (?, ?, ?)", WHO)
    conn.execute("drop table person")

# Test thread safety
class AccessThread(threading.Thread):
    def run(self):
        for i in range(1000):
            conn = sqlite3.connect("test.db")
            conn.execute("insert into person(firstname, lastname, age) values ('John', 'Doe', 42)")
            conn.commit()
            conn.close()

threads = [AccessThread() for i in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

# Test
