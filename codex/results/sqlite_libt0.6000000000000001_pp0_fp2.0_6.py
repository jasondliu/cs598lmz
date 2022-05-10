import ctypes
import ctypes.util
import threading
import sqlite3
import json
import time

# Global variables
# LibreOffice
libreoffice = ctypes.cdll.LoadLibrary(ctypes.util.find_library("libreofficekit"))

# SQLite
db = sqlite3.connect("documents.db")
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS documents(
                id INTEGER PRIMARY KEY,
                url TEXT NOT NULL,
                filename TEXT NOT NULL,
                data TEXT NOT NULL);""")

# LibO functions
libreoffice.libreofficekit_hook_function.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]
libreoffice.libreofficekit_hook_function.restype = ctypes.c_int

libreoffice.libreofficekit_callback.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
libreoffice.libre
