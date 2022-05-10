import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_void_p)

def _callback(arg, data):
    print "callback called with arg %s data %s" % (arg, data)

def py_callback():
    func = FUNTYPE(_callback)
    dll = ctypes.CDLL("./libcallback.so")
    dll.callback(func, ctypes.c_int(1), ctypes.c_void_p(2))

if __name__ == "__main__":
    py_callback()
