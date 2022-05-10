import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)

class TestThread(threading.Thread):
    def run(self):
        con = sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
        cur = con.cursor()
        cur.execute('select * from test')
        print(cur.fetchone())
        cur.close()
        con.close()

def main():
    con = sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
    cur = con.cursor()
    cur.execute('create table test (id integer)')
    cur.execute('insert into test (id) values (1)')
    cur.close()
    con.commit()
    con.close()

    threads = []
    for i in range(10):
        threads.append(TestThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name
