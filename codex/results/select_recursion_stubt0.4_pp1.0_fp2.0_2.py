import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    f.fileno()
    raises(IndexError, select.select, [f], [], [])

def test_select_keyboardinterrupt():
    import signal
    import os
    import time
    import select

    def handler(signum, frame):
        pass

    signal.signal(signal.SIGINT, handler)
    with open(os.devnull, 'r') as f:
        for i in range(100):
            time.sleep(0.01)
            select.select([f], [], [], 0)

def test_select_error():
    import os
    import select

    fd = os.open(os.devnull, os.O_RDONLY)
    try:
        select.select([fd], [], [], 0)
    finally:
        os.close(fd)

def test_select_error_2():
    import os
    import select

    fd = os.open(os.devnull, os.O_RDONLY)

