import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    try:
        select.select([], [], [])
    except ValueError:
        pass
    a.pop()
    try:
        select.select([], [], [])
    except ValueError:
        pass

def test_select_large_fd():
    class F:
        def fileno(self):
            return sys.maxsize
    try:
        select.select([F()], [], [])
    except ValueError:
        pass

def test_select_large_timeout():
    select.select([], [], [], sys.maxsize)

def test_select_negative_timeout():
    try:
        select.select([], [], [], -1)
    except ValueError:
        pass

def test_select_non_integer_timeout():
    try:
        select.select([], [], [], 1.5)
    except TypeError:
        pass

def test_select_bad_fd():
    # Issue #10100
    class F:
       
