import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
cos_func = FUNTYPE(cos)
print(cos_func(0.5))
cos_func.argtypes = [ctypes.c_float]
print(cos_func(0.5))

print()

# =====================================================
# ctypes: callbacks and callbacks from C++
# =====================================================
def callback_func(x):
    return x**2

callback_type = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
callback_func_c = callback_type(callback_func)

lib = ctypes.cdll.LoadLibrary('../cpp/libcpplib.so')
extern_callback = lib.extern_callback
extern_callback.argtypes = [callback_type]
extern_callback.restype = ctypes.c_double

print(extern_callback(callback_func_c, 2.0))

# ============================
# ctypes: passing structs
# ============================
p = (1,
