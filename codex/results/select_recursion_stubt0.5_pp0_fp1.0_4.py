import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
        def read(self):
            a.append(1)
            return 'x'

    f = F()
    select.select([f], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 1
        def read(self):
            a.append(1)
            return 'x'

    f = F()
    select.select([f], [], [], 1)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 1
        def read(self):
            a.append(1)
            return 'x'

    f = F()
    select.select([f], [], [], 1.0)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return
