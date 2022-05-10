import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    f = F()

    a.append(f)
    f = F()
    select.select([], [], [], 1e-5)
    a.append(f)

def test_select_mutated1():
    a = []

    class F:
        def fileno(self):
            test_select_mutated1()
            return 0
    f = F()

    a.append(f)
    f = F()
    select.select([], [], [], 1e-5, 1e-5)
    a.append(f)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 0
    f = F()

    a.append(f)
    f = F()
    select.poll()
    a.append(f)
