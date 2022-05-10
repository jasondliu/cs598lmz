import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a = [f]
    try:
        select.select([f], [], [])
    except IndexError:
        pass
    else:
        assert False, "select didn't raise an IndexError"

    a = [f]
    try:
        select.select([], [f], [])
    except IndexError:
        pass
    else:
        assert False, "select didn't raise an IndexError"

    a = [f]
    try:
        select.select([], [], [f])
    except IndexError:
        pass
    else:
        assert False, "select didn't raise an IndexError"

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a = [f]
    try:
        select.select([f], [], [])
    except IndexError:
        pass
    else:
        assert False, "select didn't raise an IndexError
