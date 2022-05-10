import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 2

    select.select([], [F()], [])
    assert a == []

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 2

    select.select([], [F()], [])
    assert a == [1]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 2

    select.select([], [F(), F()], [])
    assert a == [1, 1]
