import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

        def close(self):
            a.append(2)

    class F2:
        def fileno(self):
            return 2

    f = F()
    f2 = F2()
    select.select([f, f2], [], [])
    assert a == [1, 2, 1, 2]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

        def close(self):
            a.append(2)

    class F2:
        def fileno(self):
            return 2

    f = F()
    f2 = F2()
    select.select([f, f2], [], [])
    assert a == [1, 1]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

        def close(self):
            a.append(
