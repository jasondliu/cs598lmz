import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return f.fileno()

    f = F()
    a.append(f)

    fd = f.fileno()
    r, w, x = select.select([fd], [fd], [fd], 0)
    assert r == []
    assert w == [fd]
    assert x == []

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return f.fileno()

    f = F()
    a.append(f)

    fd = f.fileno()
    r, w, x = select.select([fd], [fd], [fd], 0)
    assert r == []
    assert w == [fd]
    assert x == []

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            if a:
                test_select_mutated2()
                return f.fileno()
            else:
                return f.fileno()

    f = F()
    a.append(f)
