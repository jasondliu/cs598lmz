import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    try:
        select.select([], [], a, 1)
    except ValueError:
        pass

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    a.append(F())

    try:
        select.select([], [], a, 1)
    except ValueError:
        pass

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return 0

    a.append(F())

    try:
        select.select([], [], a, 1)
    except ValueError:
        pass

    a.append(F())

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            return 0

    a.append(F())

    try:
        select.select([], [], a, 1)
    except ValueError:
        pass
