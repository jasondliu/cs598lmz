import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    a.append(F())

    try:
        select.select([], [], a, 0.0)
    except ValueError:
        pass

def test_select_error():
    a = []

    class F:
        def fileno(self):
            return 1
    a.append(F())

    try:
        select.select([], [], a, 0.0)
    except ValueError:
        pass
    else:
        raise AssertionError

def test_select_bad_return():
    class F:
        def fileno(self):
            return "abc"
    try:
        select.select([F()], [], [], 0.0)
    except ValueError:
        pass
    else:
        raise AssertionError

def test_select_bad_args():
    try:
        select.select([], [], [], "not a float")
    except TypeError:
        pass
    else:
        raise AssertionError

def test_select_bad_args2():
    try
