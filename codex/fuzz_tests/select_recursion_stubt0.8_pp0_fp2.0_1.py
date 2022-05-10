import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            # this should create a cycle
            a.append(self)
            return 42

    f = F()
    sel = select.select([f], [], [], 1.0)
    assert sel == ([], [], [])

    if hasattr(sys, "getrefcount"):
        assert sys.getrefcount(f) == 4
        del a[:]
        import gc; gc.collect()
        assert sys.getrefcount(f) == 2
        del f
        import gc; gc.collect()
    else:
        pass
