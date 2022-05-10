import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    a.append(a[0])

    select.select(a, [], [])


def test_select_mutated_empty():
    a = []

    class F:
        def fileno(self):
            self.b.append(F())

    a.append(F())
    a.append(a[0])
    a[0].b = a

    select.select(a, [], [])


def test_select_mutated_noblock():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    a.append(a[0])

    select.select(a, [], [], 0.0)
