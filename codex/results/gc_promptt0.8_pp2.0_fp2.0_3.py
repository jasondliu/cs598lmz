import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in a subinterpreter
def check():
    gc.collect() # must not crash or hang
def test():
    import _testcapi
    mod = _testcapi.make_capsule("hello")
    # make sure a weakref fires
    wr = weakref.ref(mod)
    del mod
    gc.collect()
    # make sure it's still alive
    print("wr() is", wr())
check_py3k_warnings = (3, 0) <= sys.version_info < (3, 2)

@pypytest.skip("Weakrefs are not supported in micropython")
def test_weakref_during_collection():
    it = range(2)
    def check():
        excinfo = None
        garbage = []
        try:
            while True:
                dst = []
                garbage.append(dst)
                # append some objects to dest, then check the refcounts
                for i in it:
                    o = []
                    dst.append(o)
                    # allocate more and more to be sure that the weakref
