import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections are thread safe


# Create a database connection, acquire a lock and then release it.
def worker(dbcon):
    cursor = dbcon.cursor()
    cursor.execute("SELECT * FROM R1")
    con.commit()
    cursor.close()

# Create two database connections and two threads.
con = sqlite3.connect(":memory:")
cursor = con.cursor()
cursor.execute("CREATE TABLE R1(C1, C2)")
cursor.execute("INSERT INTO R1 VALUES(1, 2)")
con.commit()
cursor.close()

con2 = sqlite3.connect(":memory:")
t1 = threading.Thread(target=worker, args=(con,))
t2 = threading.Thread(target=worker, args=(con2,))

t1.start()
t2.start()

t1.join()
t2.join()

cursor = con.cursor()
cursor.execute("SELECT COUNT(*) FROM R1")
count = cursor.fetchone()
