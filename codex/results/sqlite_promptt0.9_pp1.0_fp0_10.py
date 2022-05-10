import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("create table t1 (i, j)")
c.execute("insert into t1 values (1, 2)")

def reader():
    c2 = conn.cursor()
    c2.execute("select * from t1")
    print c2.fetchall()

threading.Thread(target=reader).start()

c.execute("insert into t1 values (3, 4)")
conn.commit()
</code>

