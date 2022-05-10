import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(F())

    select.select([], [], [], 0.0)
    f()
    select.select([], a, [], 0.0)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    def f():
        a.append(F())

    select.select([], [], [], 0.0)
    f()
    select.select([], [], a, 0.0)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_3()
            return 0

    def f():
        a.append(F())

    select.select([], [], [], 0.0)
    f()
    select.select(a, [], [], 0.0)

def test_select_mutated_4():
    a = []

   
