import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    select.select([F()], [], [])

    assert a == [1]

def test_select_keyboardinterrupt():
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    raises(KeyboardInterrupt, select.select, [], [], [], 0.1)

def test_select_timeout():
    import time
    before = time.time()
    select.select([], [], [], 0.1)
    after = time.time()
    assert after - before >= 0.1

def test_select_timeout_0():
    import time
    before = time.time()
    select.select([], [], [], 0)
    after = time.time()
    assert after - before < 0.01

def test_select_timeout_negative():
    import time
    before = time.time()
    select.select([], [], [], -0.1)
    after = time.time()
    assert after - before
