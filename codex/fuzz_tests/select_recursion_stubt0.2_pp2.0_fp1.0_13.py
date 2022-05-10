import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])
    a.append(None)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return len(a)

    select.select([F()], [], [])
    a.append(None)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return len(a)

    select.select([F()], [], [])
    a.append(None)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_4()
            return len(a)

    select.select([F()], [], [])
    a.append(None)

def test_select_mutated_5():
    a = []

    class
