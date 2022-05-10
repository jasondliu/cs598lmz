import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], [], [], 1)
    a.append(1)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    select.select([F()], [], [], 1)
    assert a == [1]


def test_select_mutated3():
    a = []
    def fselect(a, b, c, d):
        a.append(1)

    class F:
        def fileno(self):
            return 1

    fselect = select.select
    select.select = fselect

    select.select([F()], [], [], 1)
    assert a == [1]
    select.select = fselect


def test_select_mutated4():
    a = []
    def fselect(a, b, c, d):
        a.append(1)

    class F:
        def fileno(self):
            return 1

        def select(self,
