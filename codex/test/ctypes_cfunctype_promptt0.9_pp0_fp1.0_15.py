import ctypes
# Test ctypes.CFUNCTYPE
def testCFUNCTYPE():
    FUNCTYPE = ctypes.CFUNCTYPE
    @FUNCTYPE(ctypes.c_void_p)
    def restype(result):
        print("result is %d" % result)
    @FUNCTYPE(None, c_int)
    def argtypes(arg):
        print("arg is %d" % arg)
    testCFUNCTYPE = FUNCTYPE(None, c_int)
    testCFUNCTYPE(1)
    testCFUNCTYPE(restype)
    testCFUNCTYPE(argtypes)

# Test ctypes.POINTER
def testPOINTER():
    POINTER = ctypes.POINTER
    PPOINTER = POINTER(POINTER)
    int_ptr = POINTER(ctypes.c_int)
    int_pptr = PPOINTER(ctypes.c_int)
    testPOINTER = POINTER(POINTER(ctypes.c_int))
    testPOINTER(int_ptr)
    testPOINTER
