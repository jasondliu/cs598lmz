import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 1)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 4

    try:
        select.select([F()], [], [], 1)
    except TypeError:
        pass

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 4

    try:
        select.select([], [F()], [], 1)
    except TypeError:
        pass

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 4

    try:
        select.select([], [], [F()], 1)
    except TypeError:
        pass
