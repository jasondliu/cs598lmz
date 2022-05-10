import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a = [f]
    select.select([f], [], [])
    a = [f]
    select.select([], [f], [])
    a = [f]
    select.select([], [], [f])
    a = [f]
    select.select([f], [f], [f])

def test_select_keyboardinterrupt():
    # Issue #11647: select() must be interruptible with Ctrl-C
    # (or any other exception)
    def raiser():
        raise KeyboardInterrupt
    a = []
    class F:
        def fileno(self):
            a.append(1)
            return 4
    f = F()
    a = [f]
    try:
        select.select(a, a, a, 0.001)
    except KeyboardInterrupt:
        pass
    else:
        raise TestFailed("expected KeyboardInterrupt")
    #
    a = [f]
