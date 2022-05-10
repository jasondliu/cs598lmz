import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
db = sqlite3.connect(":memory:")
curs = db.cursor()
curs.execute("create table test(x)")
curs.execute("insert into test(x) values (1)")
db.commit()
curs.execute("select x from test")
print(curs.fetchone())
db.close()
# Test sqlite3.connect() with timeout
db = sqlite3.connect(":memory:", timeout=5.0)
print(db.get_timeout())
db.close()
# Test sqlite3.connect() with isolation_level
db = sqlite3.connect(":memory:", isolation_level="EXCLUSIVE")
print(db.isolation_level)
db.close()
# Test sqlite3.connect() with check_same_thread
db = sqlite3.connect(":memory:", check_same_thread=False)
db.close()
# Test sqlite3.connect() with uri
db = sqlite3.connect(":memory:", uri=True)
db.close()
#
