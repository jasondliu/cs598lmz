import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    f = F()
    try:
        select.select([f], [f], [f])
    except IndexError:
        pass

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return a.pop()
    f = F()
    try:
        select.select([f], [f], [f], 0)
    except IndexError:
        pass

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return a.pop()
    f = F()
    try:
        select.select([f], [f], [f], 0, 0)
    except IndexError:
        pass

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_4()
            return a.pop
