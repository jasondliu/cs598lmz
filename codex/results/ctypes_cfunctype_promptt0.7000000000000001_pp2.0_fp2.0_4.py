import ctypes
# Test ctypes.CFUNCTYPE with a function which returns an array.
def testit():
    print("Test of ctypes.CFUNCTYPE with non-pointer return type")
    try:
        c_int = ctypes.c_int
        c_int_p = ctypes.POINTER(c_int)
        c_int_array = ctypes.c_int * 10
        c_int_array_p = ctypes.POINTER(c_int_array)
        def f(n):
            print("f called with %d" % n)
            r = c_int_array()
            for i in range(n): r[i] = i
            return r
        CFUNCTYPE = ctypes.CFUNCTYPE
        ftype = CFUNCTYPE(c_int_array, c_int)
        fp = ftype(f)
        print("f is %r" % f)
        print("fp is %r" % fp)
        print("call fp(3)")
        r = fp(3)
        print("returned %r
