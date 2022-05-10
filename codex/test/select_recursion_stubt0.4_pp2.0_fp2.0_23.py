import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append("a")
            return a.pop()

    select.select([F()], [], [])

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append("a")
            test_select_mutated_3()
            return a.pop()

    select.select([F()], [], [])

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.append("a")
            return a.pop()

    try:
        select.select([F()], [], [], 0)
    except select.error:
        pass

def test_select_mutated_5():
    a = []

