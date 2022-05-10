import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() before we call directly
try:
    conn = sqlite3.connect("/doesnotexist")
    conn.close()
except:
    print("Getting An Error from sqlite3.connect() :" + str(sys.exc_info()))
    print("Most likely this means it won't load the ctypes sqlite3 lib")
    # FAIL
    sys.exit(1)

class NativeSqlite3(object) :

    sqlite3_lib = None

    class sqlite3_base(ctypes.Structure) :
        _fields_ = [(' version ', ctypes.c_int),
                    (' flags ', ctypes.c_int),
                    (' errstr ', ctypes.c_char_p),
                    (' utf8 ', ctypes.c_int),
                    (' user_data ', ctypes.c_void_p),
                    (' max_blobsize ', ctypes.c_long),
                    (' max_buffer_size ', ctypes.c_long),
                    (' busy_timeout ', ctypes.c_int),
                    (' busy_handler ',
