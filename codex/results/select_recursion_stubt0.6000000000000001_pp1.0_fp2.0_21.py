import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def __call__(self):
            a.append(1)

    select.select([F()], [], [], 0.1)


def test_select_negative():
    # Issue #11863, select.select raises ValueError on negative timeout
    select.select([], [], [], -1)
    select.select([], [], [], -1.0)
    select.select([], [], [], -1.0)
    select.select([], [], [], -1.0)


def test_select_keyboardinterrupt():
    import signal
    import os
    import select
    import sys

    # Issue #13228: select.select should raise KeyboardInterrupt
    # on SIGINT (or SIGBREAK on Windows).
    def handler(signum, frame):
        pass

    if sys.platform == 'win32':
        signal.signal(signal.SIGBREAK, handler)
    else:
        signal.signal(signal.SIGINT, handler)

    try:
       
