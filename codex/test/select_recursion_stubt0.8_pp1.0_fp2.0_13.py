import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 999
        def close(self):
            a.append(1)
        def do_something(self):
            pass

    f = F()
    r, w, x = select.select([f], [], [], 0)
    assert r == [f]
    assert not w and not x
    f.do_something()
    assert a == [1]

    # Issue #2116
    assert hasattr(f, "close")

    class FileLike:
        def fileno(self):
            return 0
        def close(self):
            a.append(1)
        def do_something(self):
            pass

    f = FileLike()
    r, w, x = select.select([f], [], [], 0)
    assert r == []
    assert not w and not x
    f.do_something()
    assert a == [1, 1]

    # The fd is closed when the select returns
    class FileLike:
        def fileno(self):
            return 0
