import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

    def f():
        a.append(1)
        select.select([F()], [], [])

    f()
    raises(ValueError, f)

def test_select_keyboardinterrupt():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 5

    def f():
        a.append(1)
        select.select([F()], [], [], 10)

    raises(KeyboardInterrupt, f)
    assert a

def test_select_interrupt():
    import os
    import signal
    import select
    import sys
    import threading
    import time

    # this test is flaky on Windows
    if sys.platform == 'win32':
        skip('test flaky on Windows')

    # this test is flaky on FreeBSD
    if sys.platform.startswith('freebsd'):
        skip('test flaky on FreeBSD')

    # this test is flaky on OS X
    if sys.platform == 'darwin':
        skip
