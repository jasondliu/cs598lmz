import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    try:
        select.select([F()], [], [])
    except IndexError:
        pass

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return a[0]

    try:
        select.select([F()], [], [], 0)
    except IndexError:
        pass

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return a[0]

    try:
        select.select([F()], [F()], [], 0)
    except IndexError:
        pass

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return a[0]

    try:
        select.select([F()], [F()], [F()], 0)
    except
