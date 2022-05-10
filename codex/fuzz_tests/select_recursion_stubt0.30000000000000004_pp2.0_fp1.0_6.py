import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 5

    select.select([F()], [], [], 0)
    assert a == [1]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            a.append(1)
            return 5

    select.select([F()], [], [], 0)
    assert a == [1]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            a.append(1)
            return 5

    select.select([F()], [], [], 0)
    assert a == [1]

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            a.append(1)
            return 5

    select.select([F()], [], [], 0)
    assert a == [
