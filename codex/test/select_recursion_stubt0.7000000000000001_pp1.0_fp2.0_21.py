import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            raise OSError()

        def read(self):
            a.append(self)
            return b'x'

    f = F()
    test_select_mutated()
    try:
        select.select([f], [], [], 1)
        test_select_mutated()
        f.read()
        test_select_mutated()
        f.read()
        test_select_mutated()
    except OSError:
        pass
    test_select_mutated()
    assert len(a) == 2
    test_select_mutated()
    assert a[0] is a[1]
    test_select_mutated()

def test_select():
    test_select()
    test_select()
    test_select()
    s, o, e = select.select([], [], [], 0)
    test_select()
    assert s == o == e == []
    test_select()
    s, o, e = select.select([], [], [], 1)
    test_select()
