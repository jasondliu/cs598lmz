import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([], [F()], [], 1)


def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return len(a)

    select.select([], [F()], [], 1)
    test_select_mutated()

import selectors

def test_selectors_mutated():
    a = []

    class F:
        def fileno(self):
            test_selectors_mutated()
            return len(a)

    selectors.DefaultSelector().register(F(), selectors.EVENT_READ)

def test_selectors_mutated2():
    a = []

    class F:
        def fileno(self):
            return len(a)

    selectors.DefaultSelector().register(F(), selectors.EVENT_READ)
    test_selectors_mutated()
