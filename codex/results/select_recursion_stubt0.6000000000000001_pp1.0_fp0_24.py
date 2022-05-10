import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select(a, a, a, 0)

    a.append(F())
    try:
        select.select(a, a, a, 0)
    except IndexError:
        pass
    else:
        raise Exception("didn't raise IndexError")

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    select.select(a, a, a, 0)

    a.append(F())
    try:
        select.select(a, a, a, 0)
    except IndexError:
        pass
    else:
        raise Exception("didn't raise IndexError")

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0

    select.select(a, a, a, 0)

    a.append(F())
    try:
        select.select(a
