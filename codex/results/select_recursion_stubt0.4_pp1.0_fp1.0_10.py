import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    select.select([], [], a, 0)
    a.pop()

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return -1

    a.append(F())
    select.select([], [], a, 0)
    a.pop()

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return -1

    a.append(F())
    a.append(F())
    select.select([], [], a, 0)
    a.pop()
    a.pop()

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return -1

    a.append(F())
    a.append(F())
    select.select([], [], a, 0)
    a
