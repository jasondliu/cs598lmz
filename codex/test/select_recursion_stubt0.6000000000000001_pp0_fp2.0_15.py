import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [], 0)
    assert a == [1]

def test_select_cannot_mutate():
    a = []

    class F:
        def fileno(self):
            return 1

    select.select([F()], [], [], 0)
    assert a == []

def test_select_cannot_mutate_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    select.select([F()], [], [], 0)
    assert a == [1]

def test_select_cannot_mutate_3():
    a = []

    class F:
        def fileno(self):
            return 1

        def __del__(self):
            a.append(1)

    select.select([F()], [], [], 0)
    assert a == [1]
