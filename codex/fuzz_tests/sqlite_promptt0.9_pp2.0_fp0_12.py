import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect, sqlite3.Row
class sqlite3_Row(sqlite3.Row):
    def __init__(self, *args):
        self.args = args

    def __getitem__(self, item):
        '''因为每次取值做了强转，避免大量item出现强转为tuple报错。
        sqlite3库本身就会强转类型，所以这里不需要做强转。
        '''
        return self.args[item]

    def __repr__(self):
        return str(self.args)

    def keys(self):
        return tuple([0])

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self) <= 0:
            raise StopIteration()
        val
