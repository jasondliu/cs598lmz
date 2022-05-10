import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a)

def test_select_changed_size():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return 0

    select.select([F()], a, a)
