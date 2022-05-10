import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)

def test_select_keyboardinterrupt():
    try:
        select.select([], [], [], 0)
    except KeyboardInterrupt:
        pass
    else:
        raise Exception("expected KeyboardInterrupt")

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return 0

    p = select.poll()
    p.register(F())
    p.poll(0)

def test_poll_keyboardinterrupt():
    try:
        p = select.poll()
        p.poll(0)
    except KeyboardInterrupt:
        pass
    else:
        raise Exception("expected KeyboardInterrupt")
