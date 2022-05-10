import ctypes
# Test ctypes.CFUNCTYPE for callbacks.
# FOO_CB_SIG = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER([ctypes.c_int]))
# FOO_CB_SIG = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
FOO_CB_SIG = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def foo_cb_callable(arr):
    print(arr[0], arr[1])
    return 1

# foo_cb = FOO_CB_SIG(foo_cb_callable)

# # foo_cb.argtypes = None
# foo_cb.restype = ctypes.c_int

# a_arr = (ctypes.c_int*2)(10, 20)
# a_arr = ctypes.byref(a_result)
# foo_cb(a_arr)

# # foo_cb = ctypes.CFUNCTYPE
