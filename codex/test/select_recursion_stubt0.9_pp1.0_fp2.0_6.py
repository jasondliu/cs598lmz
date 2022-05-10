import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def g():
        select.select([F()], [], [])
        a.append(None)

    try:
        g()
    except RuntimeError:
        pass

    if a:
        raise AssertionError(a)

def test_bug737473():
    # Walker's algorithm #8 didn't handle subclasses of str well
    select.select(["ass"], [], [], 0)
