import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with a string

# This is not the test you are looking for. This is a preliminary test to
# see if the connection works. Other tests should be written to see if the
# connection works with:
# 
#     * A \\?\ prefix
#     * An empty string (first part of test)
#     * A wide string
#     * A URI string
#     * A URI string with a \\?\ prefix
#     * A URI string with a wide string
#     * A URI string with an empty string
# 
# Also, the cursor methods should be tested.

db = sqlite3.connect("")
cur = db.cursor()
for word in "one", "two", "three":
    cur.execute("insert into t1 (one) values (?)", (word,))
cur.execute("select * from t1")

# not testing the results of the select
while True:
    row = cur.fetchone()
    if not row:
        break

cur.close()
db.close()
