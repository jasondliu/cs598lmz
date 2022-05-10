import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("didn't raise ValueError")


def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 42

        def close(self):
            a.append(1)

    f = F()
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    else:
        raise AssertionError("didn't raise ValueError")

    assert a == [1], a

def test_select_closed_2():
    a = []

    class F:
        def fileno(self):
            return 42

        def close(self):
            a.append(1)

    f = F()
    try:
        select.select([f], [f], [f], 0)
    except ValueError:
        pass
    else:
        raise AssertionError("didn't
