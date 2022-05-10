import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a)
    select.select(a, [F()], a)
    select.select(a, a, [F()])

def test_select_mutated_2():
    class F:
        def fileno(self):
            return 0

    select.select([F()], [F()], [F()])

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F()], a, a)
    select.select(a, [F()], a)
    select.select(a, a, [F()])

def test_select_mutated_4():
    class F:
        def fileno(self):
            return 0

    select.select([F()], [F()], [F()])
