import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# Create a new database
# conn = sqlite3.connect('test.db')

# Create a memory database
conn = sqlite3.connect(":memory:")
print "Opened database successfully";

# Create table
conn.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table created successfully";

# Insert a row of data
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

# Save (commit) the changes
conn.commit()
print "Records created successfully";

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


# import ctypes
# import ctypes.
