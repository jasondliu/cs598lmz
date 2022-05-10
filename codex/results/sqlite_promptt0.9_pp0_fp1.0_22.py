import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect database_name


class Locker(object):
    """
    Initialize the database,
    and get the cursor of database.
    """
    def __init__(self):
        """
        Database has table contains:
        id: the index of data
        data: the data
        crc: the crc of data
        """
        # Initialize the database, and set the name to be "lockmap"
        self.conn = sqlite3.connect("lockmap")
        self.curs = self.conn.cursor()

        # Create the table, if has not been create before
        self.curs.execute(
            "CREATE TABLE IF NOT EXISTS lockmap"
            "(id INT PRIMARY KEY     NOT NULL, "
            "data           TEXT    NOT NULL, "
            "crc            TEXT    NOT NULL);")

        self.locks = defaultdict(threading.Lock)
        self.locker_lock = threading.Lock()


    def get_locks(self):
        """
        Get the lock data in database.
        """
        self
