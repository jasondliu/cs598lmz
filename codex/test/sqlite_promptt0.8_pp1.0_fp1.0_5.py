import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file:memdb1?mode=memory&cache=shared", uri=True)
# Test also with fallback to in-memory


def setup_module():
    if sqlite3.sqlite_version_info < (3, 3, 4):
        pytest.skip("skipping due to sqlite version %r" %
                    sqlite3.sqlite_version)


class TestConnection(object):
    def test_detect_types(self):
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE test(
                t timestamp,
                d date,
                ts datetime
            )
        """)
        cur.execute("insert into test(t) values (?)", (datetime.now(),))
        cur.execute("insert into test(d) values (?)", (date.today(),))
        cur.execute("insert into test(ts) values (?)", (datetime.now(),))
        cur.execute("select t, d, ts from test")
        row = cur
