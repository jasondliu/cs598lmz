import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    a.append(1)
    select.select([F()], [], [], 0)

    a.append(2)
    try:
        select.select([F()], [], [], 0)
    except IndexError:
        pass
    else:
        raise Exception("didn't raise IndexError")


def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return a.pop()

    a.append(1)
    select.select([F()], [], [], 0)

    a.append(2)
    try:
        select.select([F()], [], [], 0)
    except IndexError:
        pass
    else:
        raise Exception("didn't raise IndexError")


def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return a.pop()

    a.append(1)
