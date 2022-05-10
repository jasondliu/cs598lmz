import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 0

    select.select([F()], [], [], 0)
    assert a[0] is not a[1]
    assert a[0] is not a[2]
    assert a[1] is not a[2]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            a.append(self)
            return 0

    select.select([F()], [], [], 0)
    assert a[0] is not a[1]
    assert a[0] is not a[2]
    assert a[1] is not a[2]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            a.append(self)
            return 0

    select.select([F()], [], [], 0)
    assert a[0] is not a[1]
