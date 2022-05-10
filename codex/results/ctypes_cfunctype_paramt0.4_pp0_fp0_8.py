import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

def py_callback(data):
    print("hello")

def main():
    lib = ctypes.CDLL("./libtest.so")
    lib.test_callback.argtypes = [FUNTYPE]
    lib.test_callback(FUNTYPE(py_callback))

if __name__ == "__main__":
    main()
