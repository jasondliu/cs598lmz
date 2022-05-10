import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

# If this is not a debug build, use _PY_CALL_THUNK_O which uses an offset
# instead of an absolute address.  If that is not available, assume that
# sizeof(void *) == sizeof(int).
if not hasattr(ctypes, '_PY_CALL_THUNK_O'):
    CALL_THUNK_O_SIZE = 4
    if struct.calcsize('P') != 4:
        raise ValueError('In debug build only')
else:
    CALL_THUNK_O_SIZE = struct.calcsize('P')

# Fill in the offset for _PY_CALL_THUNK_O
if hasattr(ctypes, '_PY_CALL_THUNK_O'):
    ctypes._PY_CALL_THUNK_O._offset = ctypes.cast(
            ctypes.CFUNCTYPE(ctypes.c_int)(int_func), ctypes.c_void_p).value

#
# Define an
