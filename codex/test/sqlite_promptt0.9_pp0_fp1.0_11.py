import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect


def ins(db, atr1, atr2, atr3):
    cu = db.cursor()
