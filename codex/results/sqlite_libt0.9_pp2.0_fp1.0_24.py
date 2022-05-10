import ctypes
import ctypes.util
import threading
import sqlite3


class InvalidKey(Exception):
    pass


class DB(object):
    lock = threading.Lock()
    """Access local server sqlite3 database.
    :param db_name: name of the database
    :type db_name: str
    """
    __db_name = '/home/dev/vascan.db'
    __key = '(*ayA*{q3+` I4Mc4@8C*)'

    def __init__(self, db_name=__db_name, key=None):
        if key is not None:
            if len(key) == 44:
                self.__key = key
            else:
                raise InvalidKey('Key must be 44 characters long.')

        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __str__(self):
        return "Database {}".format(self.__db_name)

    def execute(self, stmt, args=None, multiple=False):
        """Execute the given SQL statement.
       
