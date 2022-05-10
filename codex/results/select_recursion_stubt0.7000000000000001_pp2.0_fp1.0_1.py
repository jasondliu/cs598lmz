import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 1

    f = F()
    res = select.select([f], [f], [f], 0)
    assert res == ([f], [f], [f])


def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(self)
            return f.fd

    f = F()
    f.fd = 1
    res = select.select([f], [f], [f], 0)
    assert res == ([f], [f], [f])


def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(self)
            return f.fd

    class FD:
        def fileno(self):
            return 1

    f = F()
    f.fd = 1
    res = select.select([f, FD()], [f, FD()], [f, FD()], 0)
    assert res == ([f], [f], [f])

