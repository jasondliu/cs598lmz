import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return 42
libmylib.fun_in_c.restype = ctypes.c_void_p
libmylib.fun_in_c.argtypes = [FUNTYPE]
handle = libmylib.fun_in_c(fun)
print(libmylib.call_fun(handle))
libmylib.release_fun(handle)
"""

"""
import ctypes
import subprocess
subprocess.call(["./setup.sh"])
libmylib = ctypes.CDLL("./mylib.so")
libmylib.fun_in_c.restype = ctypes.c_void_p
libmylib.fun_in_c.argtypes = [ctypes.c_int]
handle = libmylib.fun_in_c(42)
print(libmylib.call_fun(handle))
libmylib.release_fun(handle)
"""
"""
import subprocess
subprocess.call(["./setup.sh"])
import cffi
ffi = cffi.FFI()
with open("mylib.h")
