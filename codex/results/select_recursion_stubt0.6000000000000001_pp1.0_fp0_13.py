import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([F()], [], [])
    select.select([], [], [F()])

    test_select_mutated()

def test_select_leak():
    seen = {}
    class F:
        def fileno(self):
            assert not seen
            seen[self] = 1
            return 1
    select.select([F()], [], [])
    assert seen

def test_select_leak_2():
    import _io
    seen = {}
    class F(_io.IOBase):
        def fileno(self):
            assert not seen
            seen[self] = 1
            return 1
    select.select([F()], [], [])
    assert seen

def test_select_leak_3():
    import _io
    seen = {}
    class F(_io.IOBase):
        def fileno(self):
            assert not seen
            seen[self] = 1
            return 1
    select.select([], [F()], [])
    assert seen

def test_select
