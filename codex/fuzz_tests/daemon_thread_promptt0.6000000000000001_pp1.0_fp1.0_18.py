import threading
# Test threading daemon
import time
# Test threading
import sys
# Test threading

# Use the system's copy of sqlite3
import sqlite3

# The temporary database file
DB_FILE = "database.db"

# The location of the database file.
DB_FILE_PATH = os.path.join(os.path.dirname(__file__), DB_FILE)

# The location of the database file.
DB_FILE_PATH_TMP = os.path.join(os.path.dirname(__file__), DB_FILE + ".tmp")

# The table name for the database
TABLE_NAME = "TEST"

# The name of the database column
COLUMN_NAME = "NAME"

# The name of the database column
COLUMN_VALUE = "VALUE"

# The size of the database block
BLOCK_SIZE = 1024

# The number of threads to run
NUM_THREADS = 4

def create_database():
    """Create the database file.
    """

    # Create the database file
    open(DB_FILE_PATH,
