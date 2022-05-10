import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    class G:
        def fileno(self):
            return f.fileno()
        def close(self):
            a.append(1)

    f = F()
    g = G()

    a.append(f)
    a.append(g)
    r = select.select([f], [], [], 0)
    assert r == ([], [], []), r
    assert a == [f, 1]

def test_select_del():
    import select
    import weakref, gc

    def close(fd):
        fd.close()

    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1
        def close(self):
            pass

    f = F()
    a.append(f)
    r = select.select([f], [], [], 0)
    assert r == ([], [], []), r
    assert a == [f, 1]
    del f
    gc.collect()
    r = select.select([
