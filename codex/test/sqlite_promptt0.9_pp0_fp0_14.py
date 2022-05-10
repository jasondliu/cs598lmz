import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.execute*() with converters

try:
    lib = ctypes.CDLL(ctypes.util.find_library('c'))
except:
    skip("No 'c' library")


def converter_instancemethod(sqltype, convfunc):
    def converter(s):
        # sqltype is 'TEXT'
        return convfunc(s)
    return converter

def converter_staticmethod(sqltype, convfunc):
    def converter(s):
        # sqltype is 'TEXT'
        return convfunc(s)
    return converter

class converter_FCextension(sqlite3.Connection):
    # This converter is used when the first argument to execute
    # method is:
    #     'SELECT ? AS test'
    # and the second argument is:
    #     ('hi',)
    #
    @staticmethod
    def convfunc(x):
        return x * 2
    def converter(self, sqltype, convfunc):
        # sqltype is 'TEXT'
        return "exec-%s" % convfunc(sqltype)

