import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    f.fileno()
    a.append(f)
    try:
        select.select([], [], [])
    except ValueError:
        pass

def test_select_non_fd():
    try:
        select.select([1], [], [])
    except TypeError:
        pass

def test_select_non_fd_with_timeout():
    try:
        select.select([1], [], [], 0)
    except TypeError:
        pass

def test_select_non_fd_with_timeout_and_non_fd_timeout():
    try:
        select.select([1], [], [], "hello")
    except TypeError:
        pass

def test_select_non_fd_with_timeout_and_negative_timeout():
    try:
        select.select([1], [], [], -1)
    except ValueError:
        pass

def test_select_non_fd_with_timeout_and_float_timeout():
    try:
