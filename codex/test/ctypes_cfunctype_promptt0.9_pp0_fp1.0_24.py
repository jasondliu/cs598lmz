import ctypes
# Test ctypes.CFUNCTYPE
def c_callback(handle, channel, period, span):
    print("callback called:", handle, channel, period, span)
    return 0

