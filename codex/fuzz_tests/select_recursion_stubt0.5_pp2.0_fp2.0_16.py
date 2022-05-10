import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(42)
            return 42

    r, w, x = select.select([F()], [], [])
    assert a == [42]
    assert r == [42]
    assert w == []
    assert x == []

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(42)
            return 42

    r, w, x = select.select([F()], [], [])
    assert a == [42]
    assert r == [42]
    assert w == []
    assert x == []

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(42)
            return 42

    r, w, x = select.select([F()], [], [])
    assert a == [42]
    assert r == [42]
    assert w == []
    assert x == []

def test_select_mutated_4():
    a = []


