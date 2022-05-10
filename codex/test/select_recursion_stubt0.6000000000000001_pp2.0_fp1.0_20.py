import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    for i in range(10):
        select.select([a[0]], [], [], 0.1)

class F:
    def fileno(self):
        return 1

class G:
    def fileno(self):
        return 2

class H(F):
    pass

def test_select_error():
    try:
        select.select([1], [2], [3])
    except TypeError:
        pass
    else:
        print('expected TypeError')

    try:
        select.select([F()], [G()], [H()])
    except TypeError:
        pass
    else:
        print('expected TypeError')

def test_select_keyboardinterrupt():
    import signal
    import sys
    import os
    import time

    def handler(signal, frame):
        return

    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGALRM, handler)

