import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
# Test sqlite3.Connection
cur = conn.cursor()
cur.execute("select 1")
cur.close()
# Test sqlite3.Cursor
cur = conn.cursor()
conn.close()
# Test GIL
threading.Thread(target=lambda: 5 + 5).start()
# Test -lm
ctypes.cdll.LoadLibrary(ctypes.util.find_library("m")).sin(1.0)
# Test rt
ctypes.cdll.LoadLibrary(ctypes.util.find_library("rt")).clock_gettime(0,
                                                                      ctypes.c_void_p())
# Test dl
ctypes.cdll.LoadLibrary(ctypes.util.find_library("dl")).dlopen(b".", 1)
# Test AUDIODEV
# Test tinfo
# Test termcap
# Test pthread
# Test ncursesw
# Test readline
# Test z
# Test lzma
# Test bz2
# Test
