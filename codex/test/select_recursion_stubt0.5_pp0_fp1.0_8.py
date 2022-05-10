import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    try:
        select.select([F()], [], [], 0)
    except IndexError:
        pass

def test_select_closed():
    class F:
        def fileno(self):
            return -1

    try:
        select.select([F()], [], [], 0)
    except ValueError:
        pass

def test_select_negative():
    class F:
        def fileno(self):
            return -1

    try:
        select.select([F()], [], [], 0)
    except ValueError:
        pass

def test_select_too_high():
    class F:
        def fileno(self):
            return sys.maxsize
    try:
        select.select([F()], [], [], 0)
    except ValueError:
        pass

def test_select_non_integer():
    class F:
        def fileno(self):
            return "hello"
