import gc, weakref

def test_collect_weakref_to_iterator():
    # Bug #5288
    def test():
        def make_iter():
            yield 1
            return
        a = make_iter()
        ref = weakref.ref(a)
        del a
        gc.collect()
        assert ref() is None
    test()
    test()
    test()
