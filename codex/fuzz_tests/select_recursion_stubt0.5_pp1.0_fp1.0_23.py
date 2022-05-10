import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())
    try:
        select.select([f], [], [], 0)
    except IndexError:
        pass
    else:
        assert False, "select() didn't fail"

def test_select_interrupted():
    a = []

    class F:
        def fileno(self):
            test_select_interrupted()
            return a.pop()

    f = F()
    a.append(f.fileno())
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
    else:
        assert False, "select() didn't fail"

def test_select_error():
    a = []

    class F:
        def fileno(self):
            test_select_error()
            return a.pop()

    f = F()
    a.append(f.fileno())
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass
