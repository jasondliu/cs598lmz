import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file:memdb1?mode=memory&cache=shared", uri=True)

def get_libc():
	libc_path = ctypes.util.find_library("c")
	return ctypes.CDLL(libc_path)

def get_func_address(func):
	return ctypes.cast(func, ctypes.c_void_p).value

def get_func_name(func):
	return ctypes.cast(func, ctypes.c_void_p).value

def get_func_from_address(address):
	return ctypes.cast(address, ctypes.c_void_p).value

def get_func_from_name(name):
	return ctypes.cast(name, ctypes.c_void_p).value

def get_func_address_from_name(name):
	return ctypes.cast(name, ctypes.c_void_p).value

