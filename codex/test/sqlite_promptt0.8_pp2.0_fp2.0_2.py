import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Vars(tuple):
    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __getitem__(self, name):
        return getattr(self, name)

    def __setattr__(self, name, value):
        return setattr(self, name, value)

    def __setitem__(self, name, value):
        return setattr(self, name, value)


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        self.vars = Db(':memory:')
        self.vars.db_initialize()


class Db(object):
    def __init__(self, db):
        super(Db, self).__init__()
        self.db = db
        self.HOST_NAMES = []

