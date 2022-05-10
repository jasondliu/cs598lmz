import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    f = F()
    a.append(f)

    try:
        select.select(a, [], [])
    except OSError:
        pass
    else:
        raise TestFailed("select.select() should have raised OSError")

def test_select_bad_fd():
    a = []
    class F:
        def fileno(self):
            return 1
    f = F()
    a.append(f)
    try:
        select.select(a, [], [])
    except OSError:
        pass
    else:
        raise TestFailed("select.select() should have raised OSError")

def test_select_bad_list():
    a = []
    a.append('foo')
    try:
        select.select(a, [], [])
    except TypeError:
        pass
    else:
        raise TestFailed("select.select() should have raised TypeError")

def test_select_bad_timeout():
    a = []
