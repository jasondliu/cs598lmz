import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/Users/matthew/Desktop/test.db")

# Database access
db_path = "/Users/matthew/Library/Application Support/Spotify/Users/matthew.c.bland-user/prefs"

# If you want to use a different database, set it here
# db_path = "/Users/matthew/Desktop/test.db"

# Initialize libspotify
lib = ctypes.CDLL(ctypes.util.find_library("spotify"))

# Initialize the Spotify API
session = lib.sp_session_create(None, None)

# Set up the callbacks
callbacks = lib.sp_session_callbacks()
callbacks.logged_in = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int)(logged_in)
callbacks.logged_out = ctypes.CFUNCTYPE(None, ctypes.c_void_p)(logged_out)
callbacks.notify_main_thread = ctypes.CFUNCTY
