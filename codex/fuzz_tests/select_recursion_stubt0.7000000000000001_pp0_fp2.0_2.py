import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a = [1]
    select.select([f], [], [], 0)

    F().fileno()

    a = [2]
    select.select([f], [], [], 0)

def test_select_mutated_otherway():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a = [1]
    select.select([f], [], [], 0)

    select.select([F()], [], [], 0)

    a = [2]
    select.select([f], [], [], 0)

def test_select_mutated_otherway2():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a = [1]
    select.select([f], [], [], 0)

    select.select([F()], [], [], 0)

   
