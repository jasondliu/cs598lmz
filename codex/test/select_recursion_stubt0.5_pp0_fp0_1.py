import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 0

    select.select([F()], [], [])
    assert a == [F()]

def test_select_keyboard_interrupt():
    import os
    import threading
    import time
    import signal

    # On Windows, the SIGBREAK signal is sent to the process when the user
    # hits Ctrl+Break.  It's not possible to intercept this signal, so we
    # skip this test.
    if sys.platform == 'win32':
        py.test.skip("cannot test SIGBREAK on Windows")

    # On OS/X, the SIGINFO signal is sent to the process when the user hits
    # Ctrl+T.  It's not possible to intercept this signal, so we skip this
    # test.
    if sys.platform == 'darwin':
        py.test.skip("cannot test SIGINFO on OS/X")

    # This test is designed to catch a race condition that can occur when a
    # signal is delivered to the process while the select() call is in
    # progress.  The race
