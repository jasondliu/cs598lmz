import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    try:
        select.select(a, [], [])
    except ValueError:
        pass
    else:
        assert False, "Did not raise ValueError"

def test_select_error():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            raise OSError

    a.append(F())

    try:
        select.select(a, [], [])
    except OSError:
        pass
    else:
        assert False, "Did not raise OSError"

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0

        def close(self):
            a.remove(self)

    a.append(F())

    try:
        select.select(a, [], [])
    except ValueError:
        pass
    else:
        assert False, "Did not raise ValueError"

