import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])
    a.append(1)
    select.select([F()], [], [])
    a.append(1)
    assert a == [1, 1]

def test_select_error():
    class F:
        def fileno(self):
            raise ValueError
    try:
        select.select([F()], [], [])
    except ValueError:
        pass
    else:
        assert False, "did not raise"

def test_select_error_2():
    class F:
        def fileno(self):
            raise ValueError
    try:
        select.select([], [F()], [])
    except ValueError:
        pass
    else:
        assert False, "did not raise"

def test_select_error_3():
    class F:
        def fileno(self):
            raise ValueError
    try:
        select.select([], [], [F()])
    except ValueError:
        pass
    else:
        assert False
