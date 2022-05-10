import ctypes
# Test ctypes.CFUNCTYPE with a 'void' return type
from ctypes import cdll, CFUNCTYPE
lib = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "test_cfunctype.dll"))

lib.set_callback.restype = None
lib.set_callback.argtypes = [CFUNCTYPE(None)]

lib.call_callback()
lib.set_callback(None)

CMPFUNC = CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
lib.set_cmp_callback.restype = None
lib.set_cmp_callback.argtypes = [CMPFUNC]

lib.call_cmp_callback()
lib.set_cmp_callback(None)

lib.set_cmp_callback(CMPFUNC(lambda x, y: x - y))

lib.call_cmp_callback()
lib.set_cmp_callback(None)

lib.set_cmp_callback(CMPFUNC(lambda x, y:
