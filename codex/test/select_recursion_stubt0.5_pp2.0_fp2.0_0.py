import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def test():
        select.select([F()], [F()], [F()])

    a = [0, 1, 2]
    test()
    a = [0, 1, 2]
    test()
    a = [0, 1, 2]
    test()

def test_select_keyboardinterrupt():
    # Issue #18809: ensure that select() doesn't swallow KeyboardInterrupt
    class F:
        def fileno(self):
            raise KeyboardInterrupt

    select.select([F()], [F()], [F()])

def test_select_error():
    # Issue #18809: ensure that select() doesn't swallow other exceptions
    class F:
        def fileno(self):
            raise OSError

    with pytest.raises(OSError):
        select.select([F()], [F()], [F()])


