import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect and threading.stack_size=1024

def test_subclass():
    # Ensures that we don't segfault if someone subclasses sqlite3.Connection
    # and doesn't call the base class constructor.
    class SDKConnection(sqlite3.Connection):
        pass
    def Connect(*args):
        return SDKConnection(*args)
    con = sqlite3.connect(":memory:", factory=Connect)
    cur = con.cursor()
    cur.execute("CREATE TABLE test(i)")
    cur.execute("INSERT INTO test(i) VALUES (42)")
    cur.execute("INSERT INTO test(i) VALUES (43)")
    cur.execute("SELECT i FROM test")
    con.close()


# Test sqlite3.Connection.iterdump()
def test_iterdump():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("create table test(i)")
    cur.execute("insert into test(i) values (5)")
    con.commit
