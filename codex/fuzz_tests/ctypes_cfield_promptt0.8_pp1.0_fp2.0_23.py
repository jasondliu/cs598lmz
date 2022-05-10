import ctypes
# Test ctypes.CField
class MyStruct(ctypes.Structure):
    _fields_ = [("array", ctypes.CField * 10)]

if __name__ == "__main__":
    import test.test_support.use_resources
    with test.test_support.use_resources.check_resources(memory=600):
        import sys
        import weakref
        import gc
        # test that we can run this test enough times to exhaust
        # the address space while also freeing everything
        if sys.platform == 'win32':  # windows has a smaller address space
            count = 2000
        else:
            count = 50000
        NUMREFS = 200
        # allocate an instance
        i = MyStruct()
        # allocate a few hundred more, weakly
        refs = [weakref.ref(MyStruct()) for i in range(NUMREFS)]
        gc.collect()
        # make sure they are still alive
        for ref in refs:
            if ref() is None:
                print "weakref died too soon"
        # allocate a few hundred more, weakly
        ref
