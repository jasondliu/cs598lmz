import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1
    a.append(F())
    try:
        select.select(a, a, a)
    except ValueError:
        pass
    else:
        assert False, "select() did not raise ValueError"

def test_select_modified():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return -1
    a.append(F())
    try:
        select.select(a, a, a)
    except ValueError:
        pass
    else:
        assert False, "select() did not raise ValueError"

def test_select_modified_2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return -1
    a.append(F())
    try:
        select.select(a, a, a)
    except ValueError:
        pass
    else:
        assert False, "select() did not raise ValueError"
