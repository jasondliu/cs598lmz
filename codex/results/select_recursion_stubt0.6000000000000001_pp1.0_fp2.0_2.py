import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a = [F()]
    select.select([], [], [], 0)


def test_select_mutated_with_timeout():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_with_timeout()
            return len(a)

    a = [F()]
    select.select([], [], [], 1)


def test_select_mutated_with_timeout_int():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_with_timeout_int()
            return len(a)

    a = [F()]
    select.select([], [], [], 1.0)
