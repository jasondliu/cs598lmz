import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return a.pop()

    select.select([F()], [F()], [F()], 0.1)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return a.pop()

    select.select([F()], [F()], [F()], 1.0)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_4()
            return a.pop()

    select.select([F()], [F()], [F()], 2.0)

def test_select_mutated_5():
    a = []

    class F:
       
