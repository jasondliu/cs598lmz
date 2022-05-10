import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    while 1:
        select.select(a, [], [])

def test_select_str_fileno():
    # Fileno is a string.
    class F:
        def __init__(self):
            self.fileno = "0"
        def __del__(self):
            self.fileno = None
    a = [F()]
    try:
        select.select(a, [], [])
    except ValueError:
        pass
    else:
        raise AssertionError

def test_select_no_fileno():
    # Fileno is missing.
    class F:
        def __del__(self):
            self.fileno = None
    a = [F()]
    try:
        select.select(a, [], [])
    except ValueError:
        pass
    else:
        raise AssertionError

def test_select_closed_fileno():
    # Fileno is closed.
    class F:
        def __init__(self):
