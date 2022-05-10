import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/data/data/com.termux/files/home/storage.sqlite")
# Test sqlite3.connect("/data/data/com.termux/files/home/storage/dcim/music.sqlite")
# Test sqlite3.connect("/data/data/com.termux/files/home/storage/dcim/music.sqlite").cursor().execute("select * from sqlite_master where type='table'").fetchall()
# Test sqlite3.connect("/data/data/com.termux/files/home/storage/dcim/music.sqlite").cursor().execute("select * from music").fetchall()
# Test sqlite3.connect("/data/data/com.termux/files/home/storage/dcim/music.sqlite").cursor().execute("select * from sqlite_master where type='table'").fetchall()
# Test sqlite3.connect("/data/data/com.termux/files/home/storage/dcim/music.sqlite").cursor().execute("select * from music").fetch
