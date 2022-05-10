import ctypes
# Test ctypes.CFUNCTYPE()

@ctypes.CFUNCTYPE(None)
def callback():
    print('called callback')

lib = ctypes.CDLL('./libpycall.so')

lib.print_string('Hello, World!')

lib.call_callback(callback)

lib.free_callback(callback)

print('done')
