import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def close(self):
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return len(a)
        def close(self):
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return len(a)
        def close(self):
            test_select_closed_mutated()
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_closed_mutated_2():
    a = []

    class F:
        def fileno(self):
            return len(a)
        def close(self):
            test_select_closed_mutated_2
