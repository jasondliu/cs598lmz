import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    f = F()
    a.append(f.fileno())
    select.select([f], [], [])

def test_select_keyboardinterrupt():
    # Issue #14457: select.select() should raise KeyboardInterrupt
    # when interrupted by a signal.
    import signal
    signal.signal(signal.SIGINT, signal.default_int_handler)
    with pytest.raises(KeyboardInterrupt):
        select.select([], [], [], 0)

def test_select_keyboardinterrupt_interrupted():
    # Issue #14457: select.select() should raise KeyboardInterrupt
    # when interrupted by a signal.
    import signal
    signal.signal(signal.SIGINT, signal.default_int_handler)
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    try:
        with pytest.raises(KeyboardInterrupt):
            select.select([], [], [], 1)
    finally:
        signal.set
