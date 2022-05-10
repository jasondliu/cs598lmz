import ctypes
# Test ctypes.CFUNCTYPE
def _test_CFUNCTYPE(self):
    #
    # Test some function pointer types
    #
    cmpfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    self.failUnlessEqual(cmpfunc(2, 3), -1)
    self.failUnlessEqual(cmpfunc(40, 40), 0)
    self.failUnlessEqual(cmpfunc(-2, -2), 0)
    self.failUnlessEqual(cmpfunc(2000000000, -2000000000), 1)

    cmpfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_long, ctypes.c_long)
    self.failUnlessEqual(cmpfunc(2, 3), -1)
    self.failUnlessEqual(cmpfunc(40, 40), 0)
    self.failUnlessEqual(cmpfunc(-2, -2), 0)
    self.failUnlessEqual(cmpfunc(2000000000, -2000000000), 1)

   
