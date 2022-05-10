import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([], [F()], [], 0)
    select.select([], a, [], 0)

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_2()
            return 0

    select.select([], [F()], [], 0)
    a.append(F())
    select.select([], a, [], 0)

def test_select_unhashable():
    class F:
        def fileno(self):
            return 0
    select.select([], [F(), F()], [], 0)
    select.select([], [], [F(), F()], 0)

def test_select_refcount():
    import gc
    class F:
        def fileno(self):
            return 0
    f = F()
    gc.collect()
    del f
