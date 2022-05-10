import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

#This test tests a simple select statement
class test_select:
    def __init__(self,inName):
        print("Running simple select test")
        self.name = inName
        
    def setup(self):
        self.drop_table()
        
    def drop_table(self):
        lib_handle = ctypes.cdll.LoadLibrary("./test_dbint.so")
        lib_func = lib_handle.drop_table_builtintest
        lib_func.restype = ctypes.c_int
        lib_func.argtypes = [ctypes.c_int, ctypes.c_char_p]
        return_code = lib_func(1,"bintest")
        print("Drop table called")
        print("Return code was:",return_code)
        
        
    def run(self):
        lib_handle = ctypes.cdll.LoadLibrary("./test_dbint.so")
        lib_handle.select_data_builtintest.restype = ctypes.c_int
        lib_handle
