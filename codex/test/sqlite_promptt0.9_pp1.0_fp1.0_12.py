import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
# with concurrent.futures.ProcessPoolExecutor() as executor:


lock = threading.Lock()


def ado_thread():
    with sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True) as conn:
        curs = conn.cursor()
        curs.execute("SELECT * from mt_tbl")
        print(curs.fetchall())


def db_thread():
    with sqlite3.connect(
            './test.db', check_same_thread=False) as conn2:
        curs = conn2.cursor()
        curs.execute("PRAGMA busy_timeout=3000")
        curs.execute("ATTACH DATABASE 'file:memdb1?mode=memory&cache=shared' AS 'strag'")
        curs.execute("SELECT * from strag.mt_tbl")
        print(curs.fetchall())


