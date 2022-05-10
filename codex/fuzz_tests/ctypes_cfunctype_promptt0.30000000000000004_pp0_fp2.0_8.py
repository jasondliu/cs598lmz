import ctypes
# Test ctypes.CFUNCTYPE()

# This is a simple example of a callback function.
def py_func(arg):
    print 'Hello from a callback', arg

# This is how you would call the callback.
def main():
    # Convert the Python callback into a C callback.
    cb = ctypes.CFUNCTYPE(None, ctypes.c_int)(py_func)

    # Now call the C function, which will call the Python callback.
    lib.call_callback(cb, 123)

if __name__ == '__main__':
    main()
</code>

