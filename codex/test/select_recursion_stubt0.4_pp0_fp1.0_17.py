import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    for i in range(10):
        a.append(i)
        try:
            select.select([F()], [], [])
        except IndexError:
            pass

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return a.pop()

    for i in range(10):
        a.append(i)
        try:
            select.select([], [F()], [])
        except IndexError:
            pass

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return a.pop()

    for i in range(10):
        a.append(i)
        try:
            select.select([], [], [F()])
        except IndexError:
            pass

def test_select_mutated_4():
    a = []

