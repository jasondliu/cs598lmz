import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def close(self):
            a.pop()
        def read(self, amnt):
            return 'x' * amnt
        def readinto(self, b):
            b[:] = b'x' * len(b)

    a = [F(), F()]

    for i in range(2):
        r, w, x = select.select([a[0]], [a[1]], [])
        assert r == [a[0]]
        assert w == [a[1]]
        assert x == []
        r, w, x = select.select([], [a[1]], [])
        assert r == []
        assert w == [a[1]]
        assert x == []
