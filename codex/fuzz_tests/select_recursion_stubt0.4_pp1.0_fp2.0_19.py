import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    select.select([F()], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return a[0]

    select.select([F()], [], [], 1)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return a[0]

    select.select([F()], [], [], 1, 1)

def test_select_mutated_exc():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_exc()
            return a[0]

    try:
        select.select([F()], [], [])
    except IndexError:
        pass

def test_select_mutated_exc2():
    a = []

    class F:
        def fileno(self):
            test_select_
