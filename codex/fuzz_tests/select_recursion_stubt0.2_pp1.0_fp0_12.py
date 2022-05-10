import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], [], [])

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], [], [])

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], [], [])

def test_select_mutated_5():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], [], [])

def test_select_mutated_6():
    a = []


