import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import json

block_list_db = ctypes.c_void_p(0)
block_list_mutex = threading.Lock()

def _load_so():
    libfile = ctypes.util.find_library("adblock_rust")
    if not libfile or libfile == "":
        libfile = os.path.dirname(__file__) + "/adblock_rust.so"
    lib = ctypes.cdll.LoadLibrary(libfile)
    lib.block_list_init.argtypes = []
    lib.block_list_free.argtypes = [ctypes.c_void_p]
    lib.block_list_add_url.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    lib.block_list_add_domain.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    lib.block_list_add_script.argtypes = [ctypes.c_void_p, ctypes.c_
