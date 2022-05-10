import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect blocking thread, with https://github.com/rca/edb,
#     http://www.cis.upenn.edu/~bcpierce/unison/
# build with "ocamlopt.opt -thread -package sqlite3 threads.cmxa sqlitedb.ml -o sqlitedb"

the_name = ctypes.util.find_library("edb")
if the_name is None:
    print("No libedb?")
    the_name = "/home/hjones/Distros/rca-db/edb-sqlite3/sqlitedb"
libedb = ctypes.CDLL(the_name)
#libedb = ctypes.CDLL("/home/hjones/Distros/rca-db/edb-sqlite3/sqlitedb")
libedb.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
libedb.sqlite3_open.restype = ctypes.c_int


semaph
