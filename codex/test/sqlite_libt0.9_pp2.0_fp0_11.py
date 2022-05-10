import ctypes
import ctypes.util
import threading
import sqlite3
import cPickle as pickle
from multiprocessing import Process, Value

# Load shared library
libmend = ctypes.CDLL(ctypes.util.find_library('mend'))
def readcstr(stream):
    return str(ctypes.string_at(ctypes.c_void_p(stream.value)))
def readlist(stream):
    vs = []
    while(1):
        n = libmend.list_next(stream)
        if n==0: break
        vs.append(n)
    return vs

# Decorator for defining attributes with functionality from Mendeleev
def defineAttr(cname, restype):
    def deco(func):
        func.fptr = getattr(libmend, cname)
        func.argtypes = ctypes.c_void_p,
        func.restype = restype
        setattr(PeriodicTable, cname, func)
        return func
    return deco

class PeriodicTable(object):
    def __init__(self):
        self
