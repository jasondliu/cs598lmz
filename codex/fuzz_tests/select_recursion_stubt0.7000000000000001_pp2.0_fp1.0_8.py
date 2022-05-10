import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    select.select([sys.stdin], [], [], 5)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            return 0

    a.append(F())

    select.select([sys.stdin], [], [], 5)

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    a.append(F())

    select.select([sys.stdin], [], [], 5)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    a.append(F())

    try:
        select.select([sys.stdin], [], [], 5)
    except ValueError:
        pass
