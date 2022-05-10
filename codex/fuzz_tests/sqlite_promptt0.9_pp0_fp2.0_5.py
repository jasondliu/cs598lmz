import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("filename.sqlite")
sqlite3.connect("scans.sqlite")
# Try to locate the library.
libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c")) 

def create_db():
    try:
        conn = sqlite3.connect("scans.sqlite")
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE scan_results (
        Scan_ID  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Timestamp TEXT NOT NULL,

        Category TEXT NOT NULL,
        Risk TEXT NOT NULL,
        Virus_Name TEXT NOT NULL,
        Action TEXT NOT NULL,

        Filename TEXT NOT NULL,
        Scanned TEXT NOT NULL,
        Result TEXT NOT NULL,
        Threat TEXT NOT NULL,
        )
        """)
    except sqlite3.OperationalError:
        pass
    return True

def update_db(category, risk, virus_name, action, filename, scanned, result, threat):
    conn = sqlite3.connect("scans
