import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect.
#######################
def test_sqlite3_connect():
    # In practice it will never be necessary to call these methods,
    # but it is helpful to find out how it works.
    # For each test, we create a database, then open a connection.
    # We then connect and close the connection.
    # And we then test all the options provided.
    #
    # %%% If a database is locked and you try to open it,
    # it will not tell you that it is locked.
    # It will just fail to open it.
    # Alasdair
    #
    # This is not a test class in the true sense.
    # But it may be helpful if the code is moved.
    # Alasdair

    #Test connect
    #############
    db = sqlite3.connect(":memory:")
    db.close()
    db = sqlite3.connect("")
    db.close()
    db = sqlite3.connect("/tmp/test_db")
    db.close()
