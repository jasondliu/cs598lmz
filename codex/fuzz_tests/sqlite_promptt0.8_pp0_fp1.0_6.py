import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect, sqlite3.close, sqlite3.cursor, sqlite3.commit,
# sqlite3.rollback, sqlite3.row_factory, sqlite3.cursor.execute,
# sqlite3.cursor.fetchall, sqlite3.cursor.close,
# sqlite3.Cursor.execute, sqlite3.Cursor.fetchall, sqlite3.Cursor.close,

s_test = """
CREATE TABLE test(num int, str text);
"""

s_insert1 = """
INSERT INTO test VALUES(1, "abc");
"""

s_insert2 = """
INSERT INTO test VALUES(2, "def");
"""

s_insert3 = """
INSERT INTO test VALUES(3, "ghi");
"""

s_sqlTest1 = """
SELECT * FROM test;
"""

s_sqlTest2 = """
SELECT * FROM test WHERE num=1;
"""

s_sqlTest3 = """
SELECT * FROM test WHERE num=2;
"""

# An infinite
