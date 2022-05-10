import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    def w():
        nonlocal a
        select.select([], [F()], [], 0)

    with pytest.raises(ValueError):
        w()

def test_select_restores():
    class F:
        def fileno(self):
            return 1

    def w():
        select.select([], [F()], [], 0)

    with pytest.raises(ValueError):
        w()

    class F:
        def fileno(self):
            return 1

    def w():
        select.select([], [F()], [], 0)

    with pytest.raises(ValueError):
        w()

def test_native_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_native_select_mutated()
            return 1

    def w():
        nonlocal a
        select.select([], [F()], [], 0)

    with pytest.raises(ValueError):
        w()

