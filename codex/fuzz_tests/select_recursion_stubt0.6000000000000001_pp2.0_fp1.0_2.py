import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([F()], a, a, 10)

def test_select_keyboardinterrupt():
    a = []
    def f():
        raise KeyboardInterrupt
    class F:
        def fileno(self):
            f()
    try:
        select.select([F()], a, a, 10)
    except KeyboardInterrupt:
        pass
    else:
        raise Exception("did not raise")
