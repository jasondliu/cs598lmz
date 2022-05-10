import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection
# connection = sqlite3.connect(":memory:", check_same_thread=False)

def _check_err(status):
    if status != 0:
        raise IOError("Error: %s (%s)" %
                          (status, get_error_message(status)))

# TODO use ctypes_configure.py to generate
# LuaJIT uses Lua's C API and is compatible
class _Struct(ctypes.Structure):
    pass

class _LuaState(_Struct):
    _fields_ = [
        ('l_G', ctypes.c_void_p),
        ('l_registry', ctypes.c_void_p)
    ]

LUA_GLOBALSINDEX = -10002
LUA_REGISTRYINDEX = -10000

def get_error_message(status):
    _check_err(status)
    if status != 0:
        _check_err(status)
        return ctypes.string_at(f.lua_tolstring(self._state, -1, 0))
