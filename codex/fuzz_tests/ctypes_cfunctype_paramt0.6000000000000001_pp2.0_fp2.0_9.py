import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def test_cfunc(f):
    print(f(1, 2))

def test_ctypes_callback(f):
    f(1)

def test_ctypes_callback_byref(f):
    f(ctypes.c_int(1))

def test_ctypes_callback_byref_opt(f):
    f(ctypes.c_int(1), None)

def test_ctypes_callback_opt(f):
    f(None)

def test_ctypes_callback_opt_byref(f):
    f(None, ctypes.c_int(1))

def test_ctypes_callback_opt_byref_opt(f):
    f(None, ctypes.c_int(1), None)

def test_ctypes_callback_opt_opt_byref_opt(f):
    f(None, None, ctypes.c_int(1), None)

def test_ctypes_callback_opt_opt_byref_opt_opt(f
