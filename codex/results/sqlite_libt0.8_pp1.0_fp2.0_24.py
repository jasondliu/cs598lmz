import ctypes
import ctypes.util
import threading
import sqlite3

DB_NAME = 'media_db'

class MediaDb:
    def __init__(self):
        self.__lock = threading.RLock()
        self.__db_handle = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def open(self):
        self.__lock.acquire()

        try:
            if self.__db_handle is None:
                self.__db_handle = sqlite3.connect(DB_NAME)
        except Exception as ex:
            self.close()
            raise Exception(ex)
        finally:
            self.__lock.release()

    def close(self):
        self.__lock.acquire()

        try:
            if self.__db_handle is not None:
                self.__db_handle.close()
                self.__db_handle = None
        finally:
            self.__lock.release()

    def do_command(self, command):
        if
