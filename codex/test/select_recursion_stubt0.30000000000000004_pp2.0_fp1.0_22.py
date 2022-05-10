import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except IndexError:
        pass
    else:
        assert False, "select() didn't raise IndexError"

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return a.pop()

    f = F()
    a.append(f)
    try:
        select.select([f], [f], [f])
    except IndexError:
        pass
    else:
        assert False, "select() didn't raise IndexError"

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return a.pop()

    f = F()
    a.append(f)
