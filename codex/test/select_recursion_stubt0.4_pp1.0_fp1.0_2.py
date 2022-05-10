import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_select_bad_fd():
    class F:
        def fileno(self):
            return -1

    f = F()
    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_select_closed_fd():
    class F:
        def fileno(self):
            return 0

        def close(self):
            pass

    f = F()
    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_select_bad_list():
    try:
        select.select([1], [], [])
    except TypeError:
        pass
    try:
        select.select([], [1], [])
    except TypeError:
        pass
