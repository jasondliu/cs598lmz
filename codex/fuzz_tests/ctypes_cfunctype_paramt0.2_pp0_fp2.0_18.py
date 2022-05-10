import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("my_callback called with", x)
    return x + 1

def main():
    lib = ctypes.CDLL("./libmylib.so")
    lib.my_function.argtypes = [FUNTYPE]
    lib.my_function.restype = ctypes.c_int
    result = lib.my_function(FUNTYPE(my_callback))
    print("my_function returned", result)

if __name__ == "__main__":
    main()
</code>

