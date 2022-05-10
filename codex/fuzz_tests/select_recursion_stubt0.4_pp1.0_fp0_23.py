import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 42

    f = F()
    select.select([f], [], [])
    assert a == [1]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            a.append(1)
            return 42

    f = F()
    select.select([f], [f], [f])
    assert a == [1]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            a.append(1)
            return 42

    f = F()
    select.select([f], [f], [f], 0.1)
    assert a == [1]
