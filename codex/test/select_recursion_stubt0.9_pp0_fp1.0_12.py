import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

        def read(self):
            a.append(1)

    select.select([F()], [], [], 0.1)

    class F:
        def fileno(self):
            a.clear()

        def read(self):
            test_select_mutated()

    select.select([F()], [], [], 0.1)

def test_select_exception():
    a = []

    class F:
        def fileno(self):
            1 / 0

    select.select([F()], [], [], 0.1)

    class F:
        def fileno(self):
            a.clear()
        def read(self):
            1 / 0

    select.select([F()], [], [], 0.1)

DELAY = 0.2

