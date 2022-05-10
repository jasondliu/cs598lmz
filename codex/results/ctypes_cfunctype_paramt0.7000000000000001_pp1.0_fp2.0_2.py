import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int)

lib = ctypes.CDLL('librustpython.so')

def cb(val):
    print("callback called with", val)
    return

cb_f = FUNTYPE(cb)

def main():
    print("running callback")

    lib.callback(42, cb_f)
