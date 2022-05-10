import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    f = F()

    class S:
        def select(self, r, w, x, timeout):
            a.append(f)
            return [], [], []

    select.select = S().select

    select.select([f], [], [], 0)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 0
    f = F()

    class S:
        def select(self, r, w, x, timeout):
            a.append(f)
            return [], [], []

    select.select = S().select

    select.select([f], [], [], 0)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 0
    f = F()

    class S:
        def select(self, r, w, x, timeout):
            a.append(f)

