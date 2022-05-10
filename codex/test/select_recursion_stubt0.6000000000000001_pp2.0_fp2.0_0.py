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

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a[:] = [1]
            return a.pop()

    try:
        select.select([F()], [], [], 0)
    except IndexError:
        pass

def test_select_str():
    try:
        select.select([b'a'], [], [], 0)
    except TypeError:
        pass

def test_select_str_2():
    try:
        select.select([], [b'a'], [], 0)
    except TypeError:
        pass

def test_select_str_3():
    try:
        select.select([], [], [b'a'], 0)
    except TypeError:
        pass

