import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test ctypes.util.find_library()

def find_library(libname):
    print('find_library:', libname)
    return ctypes.util.find_library(libname)

# Test ctypes.CDLL()

def CDLL(libname):
    print('CDLL:', libname)
    return ctypes.CDLL(libname)

# Test ctypes.CDLL().__getattr__()

def getattr(lib, name):
    print('getattr:', name)
    return getattr(lib, name)

# Test ctypes.CDLL().__getattr__()()

def call(func, *args):
    print('call:', func.__name__)
    return func(*args)

# Test ctypes.CDLL().__getattr__()().restype

def restype(func, restype):
    print('restype:', restype)
    func.restype = restype

# Test ctypes.CDLL().__getattr__()().argtypes

