import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1
    f = F()
    a.append(f)
    try:
        select.select([], a, [], 0)
    except ValueError:
        pass
    else:
        assert False, 'select() should have raised ValueError'

def test_select_keyboardinterrupt():
    import signal
    signal.signal(signal.SIGINT, signal.default_int_handler)
    try:
        select.select([], [], [], 0)
    except KeyboardInterrupt:
        pass
    else:
        assert False, 'select() should have raised KeyboardInterrupt'
