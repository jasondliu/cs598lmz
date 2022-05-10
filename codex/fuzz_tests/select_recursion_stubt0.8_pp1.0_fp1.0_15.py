import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def read(self):
            a.append(1)
            return b'\0'

    s = select.select([F()], [], [])
    assert a == [], s # doesn't crash

def test_select_gc_prevented():
    # Regression test for a nasty segfault, when a select object is
    # returned by select.select(), but the referenced file descriptors
    # are garbage-collected before the object is used.
    #
    # I don't seem to find a way to force the segfault consistently,
    # especially when running PyPy in opt mode.  This test does not
    # run at all on top of CPython, as there select.select() never
    # returns a tuple (it returns a list).
    import gc
    class FD:
        def fileno(self):
            return os.open(os.devnull, os.O_RDONLY)
        def __del__(self):
            # Called after select() is over, but before FD is touched
            # again.
            gc.collect
