import ctypes
# Test ctypes.CFUNCTYPE(). To pass the test, you'll need the
# libc library.
if False:
    strchr = ctypes.CDLL(None).strchr
    CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    def mycmp(e1, e2):
        print(strchr(e1), strchr(e2))
        return e1 - e2
    # The buffer protocol is used to retrieve the address of the
    # elements.
    py_array = array('i', [5, 2, 3, 6, 8, 1, 0, 3, 5, 6])
    cmp_func = CMPFUNC(mycmp)
    c_array = (ctypes.c_int * len(py_array))(*py_array)
    res = cdll.msvcrt.qsort(c_array, len(py_array), ctypes.sizeof(c_array[0]), cmp_func)
    assert not res
