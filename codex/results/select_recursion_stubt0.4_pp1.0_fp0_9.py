import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(1)
    a.append(2)
    select.select([f], [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(1)
    a.append(2)
    select.select([f], [], [])

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(1)
    a.append(2)
    select.select([f], [], [], 0)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(1)
    a.append(2)
    select.select([f], [], [
