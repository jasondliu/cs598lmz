import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    else:
        assert False, "select() returned successfully"

def test_select_error():
    import select
    class BadFD:
        def fileno(self):
            return -1
    try:
        select.select([BadFD()], [], [])
    except ValueError:
        pass
    else:
        assert False, "select() returned successfully"

def test_select_large_fd():
    import select
    class LargeFD:
        def fileno(self):
            return 1<<31
    try:
        select.select([LargeFD()], [], [])
    except ValueError:
        pass
    else:
        assert False, "select() returned successfully"

def test_select_negative_fd():
    import select
    class NegativeFD:
        def fileno(self):
            return -1
