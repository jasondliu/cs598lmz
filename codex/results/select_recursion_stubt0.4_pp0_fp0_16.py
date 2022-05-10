import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def close(self):
            a.append(1)

    select.select([F()], [], [], 1)
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.append(1)

    select.select([F()], [], [], 1)
    assert a == [1]
