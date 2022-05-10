import ctypes
import ctypes.util
import threading
import sqlite3


class TagDB:
    """
    Tag database class, based on sqlite3.
    """

    def __init__(self, dbname):
        """
        Initialize TagDB object.
        """
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.cursor.execute("""create table if not exists tags
                             (tag text primary key,
                              count integer,
                              first_seen_time integer,
                              last_seen_time integer)""")
        self.cursor.execute("""create table if not exists tag_to_file
                             (tag text,
                              file text)""")
        self.conn.commit()
        self.lock = threading.Lock()

    def close(self):
        """
        Close the database connection.
        """
        self.conn.commit()
        self.conn.close()

    def get_file_list
