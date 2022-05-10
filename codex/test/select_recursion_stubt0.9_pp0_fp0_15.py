import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())

    test_select_mutated()
    select.select([], a, [], 1)

def test_select_state():
    def f():
        a = []

        class F:
            def fileno(self):
                return 1

        a.append(F())

        test_select_state()
        test_select_state()
        test_select_state()
        test_select_state()
        test_select_state()
        test_select_state()
        test_select_state()
        test_select_state()
        return select.select([], a, [], 1)

    for i in range(1):
        f()

def test_select_void():
    def f():
        select.select([], [], [], 1)
        return

    import gc
    while True:
        gc.collect()
        f()
        gc.collect()
        f()
        f()
        f()


