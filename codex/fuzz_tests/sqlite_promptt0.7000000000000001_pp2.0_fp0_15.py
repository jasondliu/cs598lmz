import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/Users/michael/Desktop/test.db")
# Test sqlite3.connect("test.db")



class File(object):
    def __init__(self, path, file_name=None, use_db=False, db_name="logs.db"):
        self.path = path
        self.file_name = file_name
        self.name = os.path.join(path, file_name)
        self.use_db = use_db
        self.db_name = db_name
        self.file_lock = threading.Lock()
        self.db_lock = threading.Lock()
        if self.use_db:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.text_factory = str
            self.cursor = self.conn.cursor()
            self.setup_db()

    def setup_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS log_files (
                id int primary key,
                path
