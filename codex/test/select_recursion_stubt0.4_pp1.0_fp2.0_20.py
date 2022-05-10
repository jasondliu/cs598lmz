import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

def test_select_mutated_2():
    class F:
        def fileno(self):
            raise ValueError

    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

def test_select_mutated_3():
    class F:
        def fileno(self):
            raise ValueError

    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])

def test_select_mutated_4():
    class F:
        def fileno(self):
            raise ValueError

    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])


