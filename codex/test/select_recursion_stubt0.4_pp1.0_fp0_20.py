import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()

    a = [f]
    select.select([f], [], [], 0)
    a = [f]
    select.select([f], [], [], 0)
    a = [f]
    select.select([f], [], [], 0)
    a = [f]
    select.select([f], [], [], 0)

def test_select_keyboard_interrupt():
    import signal
    import os
    import time

    def handler(signum, frame):
        pass

    signal.signal(signal.SIGINT, handler)

    for i in range(100):
        try:
            select.select([], [], [], 0.1)
        except KeyboardInterrupt:
            pass
        else:
            break
    else:
        raise Exception("Failed to raise KeyboardInterrupt")

    signal.signal(signal.SIGINT, signal.SIG_DFL)

