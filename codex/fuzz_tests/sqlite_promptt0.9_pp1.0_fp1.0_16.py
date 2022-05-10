import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with various threading options
# 2011-Feb-07 sqlite-users

sync_on = False
steps = 1

def do_work(_):
    global steps
    steps += 1
    conn.execute("INSERT INTO data (thing) VALUES (NULL);")
    conn.commit()
    if not sync_on:
        ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_get_autocommit(conn.sqlite_conn)
        

def test(reps, sync):
    global conn
    global sync_on
    global steps
    sync_on = sync
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    steps = 1
    conn.execute("PRAGMA synchronous = %d;" % int(sync))

    threads = [threading.Thread(target=do_work, args=(i,)) for i in range(reps)]
    threads.append(threading.Thread(target=conn.execute("SELECT * FROM data;")))
    #threads
