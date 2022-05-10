import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            del a[:]
            a.append(1)
            return 1

        def close(self):
            pass

    f = F()
    a.append(f)
    select.select([f], [], [])
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

        def close(self):
            a.append(2)

    f = F()
    a.append(f)
    select.select([f], [], [])
    assert a == [1, 2]

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            del a[:]
            a.append(1)
            return 1

        def close(self):
            a.append(2)

    f = F()
    a.append(f)
    select.select([f], [], [])
    assert a == [1, 2]

def test
