import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') on a command line.

# Otherwise, use this file name; you may want to change it.
# db_filename = 'todo.db'

# Call this routine when you change the todo table in any way:
# create tables, delete columns, or change types.
def reset_tables():
    """Create new, empty tables in our database.
    Delete all existing data.
    """
    with sqlite3.connect(db_filename) as conn:
        cur = conn.cursor()

        # Do not use "IF EXISTS" here, which is SQLite-specific.
        cur.execute("DROP TABLE IF EXISTS todo")
        cur.execute("""\
        CREATE TABLE todo (
            task_id    INTEGER PRIMARY KEY,
            priority   INTEGER,
            details    TEXT,
            status     INTEGER,
            deadline   TEXT
        )
        """)

        cur.execute("DROP TABLE IF EXISTS projects")
        cur.execute("""\
        CREATE TABLE projects (
           
