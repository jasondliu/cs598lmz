import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 55

    s = select.select(a + [F()], [], [])
    assert s == ([F()], [], [])
    assert a == [F()]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    a.append(55)
    a.append(56)
    a.append(57)

    s = select.select(a, [], [])
    assert s == ([], [], [])
    assert a == []

def test_select_closed_read():
    a = []

    class F:
        def fileno(self):
            try:
                return a.pop()
            finally:
                a.append(self)

    a.append(55)
    a.append(56)
    a.append(57)

    s = select.select(a, [], [])
    assert s == ([], [], [])
    assert a == [F()]

