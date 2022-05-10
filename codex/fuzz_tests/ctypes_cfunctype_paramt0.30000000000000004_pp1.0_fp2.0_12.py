import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test_callback():
    # This is the prototype of the callback function
    CALLBACK = FUNTYPE(ctypes.c_int, ctypes.c_int)

    # This is the prototype of the function that takes the callback
    # as an argument
    FUNC = FUNTYPE(None, CALLBACK, ctypes.c_int)

    # This is the actual callback function
    @CALLBACK
    def mycallback(i):
        print "called back with", i
        return i + 1

    # This is the actual function that takes the callback
    @FUNC
    def myfunc(cb, i):
        print "calling back with", i
        cb(i)

    # Call the function with the callback
    myfunc(mycallback, 42)

if __name__ == '__main__':
    test_callback()
</code>

