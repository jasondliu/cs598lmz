import ctypes
# Test ctypes.CFUNCTYPE
def c_callback(handle, channel, period, span):
    print("callback called:", handle, channel, period, span)
    return 0

lib = ctypes.cdll.LoadLibrary("libhello.dylib")
c_callback_fn = ctypes.CFUNCTYPE(ctypes.c_int,
                                 ctypes.c_int,
                                 ctypes.c_int,
                                 ctypes.c_int,
                                 ctypes.c_int)
c_callback_p = c_callback_fn(c_callback)
result = lib.c_test(100, 200, 300, ctypes.cast(c_callback_p, ctypes.c_void_p))
if result == 0:
    print("OK")
else:
    print("NG, result:", result)

# Test ctypes.POINTER
buf = ctypes.c_char_p(b'Hello World')
lib.c_pointer_test(buf)
print('got back: ' + str(buf.value.decode()))

# Test ctypes.
