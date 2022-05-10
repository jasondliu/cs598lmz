import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class Sqlite3Thread(threading.Thread):
    def __init__(self, name):
        super(Sqlite3Thread, self).__init__()
        self.name = name
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()

    def run(self):
        print("Thread %s started" % self.name)
        self.cursor.execute("CREATE TABLE test(id INTEGER PRIMARY KEY, name TEXT)")
        self.cursor.execute("INSERT INTO test VALUES(1, 'test')")
        self.cursor.execute("SELECT * FROM test")
        print("Thread %s finished" % self.name)

threads = []
for i in range(0, 10):
    thread = Sqlite3Thread(i)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("All threads finished")
</code>

