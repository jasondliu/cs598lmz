import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect with /memdb1
# memdb = "file::memory:?cache=shared"
#SQLite memory database is private per process and cannot share with other processes.
memdb = "file::memory:?cache=shared"
#memdb = ":memory:"

def thread_noop(dbid):
    while True:
        pass

db1 = sqlite3.connect(memdb)
db2 = sqlite3.connect(memdb)

# Both connection uses the same in-memory database shared in memory
db1.execute("create table data (id int primary key, data text)")
db1.execute("insert into data(id, data) values (1, 'AA')")
db1.commit()
r = db2.execute("select id, data from data where id=1")
record = r.fetchone()
print(record)

# Test to create thread in each connections
t1 = threading.Thread(target=thread_noop, args=(1,))
t2 = threading.Thread(target=thread_noop, args=(2,))
t
