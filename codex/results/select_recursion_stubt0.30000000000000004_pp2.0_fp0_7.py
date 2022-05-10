import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    s = select.select([F()], [], [])
    assert s == ([], [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    s = select.select([F()], [], [])
    assert s == ([], [], [])

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

        def close(self):
            a.pop()

    s = select.select([F()], [], [])
    assert s == ([], [], [])

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

        def close(self):
            a.pop()

    s = select.select([F
