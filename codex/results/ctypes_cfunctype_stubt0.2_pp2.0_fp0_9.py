import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# restype: 返回值类型
# *argtypes: 参数类型
# use_errno: 是否使用errno
# use_last_error: 是否使用GetLastError()

# ctypes.c_int.in_dll(ctypes.cdll.msvcrt, "errno")
# ctypes.cdll.msvcrt.GetLastError()

# ctypes.POINTER(ctypes.c_int)
# ctypes.pointer(ctypes.c_int(42))
# ctypes.byref(ctypes.c_int(42))

# ctypes.c_int32.from_address(id(ctypes.c_int32(42)))

# ctypes.c_int.from_buffer(bytear
