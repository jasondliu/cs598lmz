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

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 42

    f = F()
    select.select([f], [], [])
    assert a == [1]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 42

        def close(self):
            a.append(2)

    f = F()
    select.select([f], [], [])
    assert a == [1, 2]
