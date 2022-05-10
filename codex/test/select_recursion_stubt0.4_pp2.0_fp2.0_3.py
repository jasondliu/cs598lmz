import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    s = select.select([F()], [], [], 0)
    assert not s[0]
    assert not s[1]
    assert not s[2]

def test_select_keyboard_interrupt():
    import time
    import os
    import signal

    def handler(signum, frame):
        raise KeyboardInterrupt

    signal.signal(signal.SIGALRM, handler)

    def timeout(secs):
        signal.alarm(secs)
        time.sleep(2*secs)
        assert False, "timeout error"

    # Issue #17095: select() should be interruptible by SIGINT
    # on Windows.
    if os.name == "nt":
        timeout(10)
        try:
            select.select([], [], [], 1)
        except KeyboardInterrupt:
            pass
        else:
            assert False, "SIGINT was not received"
    else:
        timeout(1)
