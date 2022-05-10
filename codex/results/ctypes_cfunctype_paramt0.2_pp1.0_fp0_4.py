import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with", x)
    return x + 1

def main():
    # Create a callback function from the Python function
    cb = FUNTYPE(my_callback)

    # Call the C function
    c_lib.call_callback(cb)

if __name__ == "__main__":
    main()
</code>

