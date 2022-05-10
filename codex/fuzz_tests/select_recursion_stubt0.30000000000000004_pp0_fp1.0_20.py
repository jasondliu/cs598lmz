import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def close(self):
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.append(1)

    f = F()
    f.close()
    select.select([f], [], [])
    assert a == [1]

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.append(1)

    f = F()
    f.close()
    select.select([f], [], [])
    assert a == [1]

def test_select_closed_mutated_2():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.append(1)

    f = F
