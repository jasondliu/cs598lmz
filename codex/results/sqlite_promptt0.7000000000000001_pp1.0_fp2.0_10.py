import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect().
sqlite3.connect(":memory:")

# Test threading.local().
local = threading.local()
local.x = 42
assert local.x == 42

# Test ctypes.util.find_library().
libm = ctypes.util.find_library("m")
assert libm is not None

# Test ctypes.CDLL().
ctypes.CDLL(libm)

# Test ctypes.c_int.from_address().
ctypes.c_int.from_address(id(ctypes)).value

# Test ctypes.cast().
ctypes.cast(ctypes.c_int(42), ctypes.py_object).value

# Test ctypes.Pointer().
ctypes.pointer(ctypes.c_int(42))

# Test ctypes.addressof().
ctypes.addressof(ctypes.c_int(42))

# Test ctypes.string_at().
ctypes.string_at(b"hello world")

# Test ctypes.create_string_buffer().
ctypes
