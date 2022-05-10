import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.rollback() method

# This test case is designed to test sqlite3.connection.rollback()
# method, which rollbacks transaction. The test case is composed of
# two threads. One thread will rollback the transaction and the other
# one will check if the changes have been rolled back.

MITestLib = ctypes.CDLL(ctypes.util.find_library("MITestLib"))

test_rollback_lock = threading.Lock()

# This routine is executed by the second thread
def test_rollback_thread(db_name, pid):
    test_rollback_lock.acquire()
    try:
        # Connect to the database and get the number of rows
        con = sqlite3.connect(db_name)
        try:
            cur = con.cursor()
            cur.execute('SELECT COUNT(*) FROM test')
            row_count = int(cur.fetchone()[0])
            MITestLib.mi_test_db_result(pid, row_count)
            # Rollback the changes
            con.rollback()
           
