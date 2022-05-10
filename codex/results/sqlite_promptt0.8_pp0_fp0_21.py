import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# CONN = sqlite3.connect("langfod.db")
# C = CONN.cursor()
# C.execute("SELECT * FROM subjects")
# print(C.fetchall())

# Python wrapper for tts
class TextToSpeech:
    # Load libtts
    libtts = ctypes.util.find_library("tts")
    try:
        _libtts = ctypes.cdll.LoadLibrary(libtts)
    except OSError as e:
        if e.args[0] == 'image not found':
            try:
                _libtts = ctypes.cdll.LoadLibrary('/usr/lib/libtts.dylib')
            except OSError as e:
                if e.args[0] == 'image not found':
                    print("Library tts not found, to install it run: sudo apt-get install tts")
        else:
            print("Library tts not found, to install it run: sudo apt-get install tts")

    # Configure libtts
    _lib
