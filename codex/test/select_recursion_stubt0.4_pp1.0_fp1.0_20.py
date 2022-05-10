import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [], 0)

    f()
    f()

def test_select_mutated_2():
    a = []

    def f():
        a.append(1)
        select.select([], [], [], 0)

    f()
    f()

def test_select_mutated_3():
    a = []

    def f():
        a.append(1)
        select.select([], [], [], 0)

    f()
    f()

def test_select_mutated_4():
    a = []

    def f():
        a.append(1)
        select.select([], [], [], 0)

    f()
    f()

def test_select_mutated_5():
    a = []

    def f():
        a.append(1)
        select.select([], [], [], 0)

    f()
    f()

