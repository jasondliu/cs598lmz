import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [], 0.01)
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            raise IOError()

    select.select([F()], [], [], 0.01)
    assert a == [1]

def test_select_bad():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    select.select([F()], [], [], 0.01)
    assert a == [1]

def test_select_closed_other():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    select.select([], [F()], [], 0.01)
    assert a == [1]

def test_select_closed_other_2():
    a = []

