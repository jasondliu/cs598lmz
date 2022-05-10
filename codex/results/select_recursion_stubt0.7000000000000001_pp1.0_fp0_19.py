import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

        def close(self):
            test_select_mutated()

        def read(self):
            test_select_mutated()
            return a.pop()
        readinto = read

    fd = F()
    fd2 = F()
    fd3 = F()
    a[:] = [1, fd2, fd3]
    r,w,x = select.select([fd], [], [], 0)
    assert r == [fd2], r
    r,w,x = select.select([fd], [fd], [], 0)
    assert r == [fd2], r
    assert w == [fd3], w
    r,w,x = select.select([fd], [fd], [fd], 0)
    assert r == [fd2], r
    assert w == [fd3], w
    assert x == [fd], x
    r,w,x = select.select([], [], [fd], 0)
    assert x == [fd], x
