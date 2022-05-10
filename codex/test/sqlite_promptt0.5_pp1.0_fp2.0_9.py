import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# The SQLite database file name
db_name = "test.db"

# The SQLite database connection object
db_conn = None

# The SQLite database cursor object
db_cur = None

# The SQLite database table name
db_table = "test_table"

# The SQLite database table column names
db_cols = ["test_col_1", "test_col_2"]

# The SQLite database table column types
db_types = ["int", "int"]

# The SQLite database table column values
db_values = [1, 2]

# The SQLite database table column types
db_table_col_types = "("
for col_type in db_types:
    db_table_col_types += col_type + ", "
db_table_col_types = db_table_col_types[:-2] + ")"

# The SQLite database table column names
db_table_col_names = "("
for col_name in db_cols:
    db_table_col_names += col_name
