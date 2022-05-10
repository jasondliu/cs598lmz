import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    select.select([F()], [], [])
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    f = F()
    os.close(1)
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    else:
        assert 0, "Didn't raise"
    assert a == [1]

def test_waitpid_mutated():
    a = []

    class F:
        def __init__(self):
            self.pid = 1

        def __del__(self):
            a.append(1)

    F()
    os.waitpid(1, 0)
    assert a == [1]

def test_waitpid_non_integer():
    a = []

    class F:
        def __del__(self):
            a.append(1)

        def __int
