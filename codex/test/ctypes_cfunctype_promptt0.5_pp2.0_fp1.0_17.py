import ctypes
# Test ctypes.CFUNCTYPE.

if __name__ == '__main__':
    from ctypes import *

    libc = CDLL("libc.so.6")
    CallbackType = CFUNCTYPE(c_int, c_int, c_int)
    def callback(arg1, arg2):
        print("callback", arg1, arg2)
        return arg1 + arg2
    cb = CallbackType(callback)
