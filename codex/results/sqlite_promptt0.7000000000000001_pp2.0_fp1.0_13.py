import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections are thread-safe
threads = []

class TestConnection(threading.Thread):
    def run(self):
        self.con = sqlite3.connect(":memory:")
        self.cur = self.con.cursor()
        self.cur.execute("create table test(id integer)")
        self.cur.execute("insert into test(id) values (?)", (1,))
        self.cur.execute("insert into test(id) values (?)", (2,))
        self.cur.execute("select id from test order by id")
        self.result = self.cur.fetchall()

for i in xrange(100):
    t = TestConnection()
    t.start()
    threads.append(t)
for t in threads:
    t.join()
    assert t.result == [(1,), (2,)], t.result
