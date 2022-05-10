import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [])

    try:
        f()
    except RuntimeError:
        pass
    assert a == [1]

def test_select_mutated_exc():
    a = []

    class F:
        def fileno(self):
            raise ValueError
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [])

    try:
        f()
    except RuntimeError:
        pass
    assert a == [1]
