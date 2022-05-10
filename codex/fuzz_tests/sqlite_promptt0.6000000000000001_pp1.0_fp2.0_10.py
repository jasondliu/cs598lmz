import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("create table foo(x int)")
c.execute("insert into foo values (1)")
c.execute("insert into foo values (2)")
c.execute("insert into foo values (3)")
c.execute("select x from foo")
c.fetchall()

# Test sqlite3.complete_statement
sqlite3.complete_statement("select 1")

# Test sqlite3.register_adapter
sqlite3.register_adapter(int, lambda x: str(x))

# Test sqlite3.register_converter
sqlite3.register_converter("int", lambda x: int(x))

# Test sqlite3.Row
for row in c.execute("select * from foo"):
    row[0]

# Test sqlite3.Row.keys
row.keys()

# Test sqlite3.Row.values
row.values()

# Test sqlite3.Row.items
row.items()

