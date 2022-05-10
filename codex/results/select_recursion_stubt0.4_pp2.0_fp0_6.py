import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    s = select.select([F()], [], [])
    assert s == ([], [], [])
    del s
    a.append(1)
    assert a == [1]

def test_select_keyboardinterrupt():
    import select
    import signal
    import os
    import sys

    def handler(signum, frame):
        pass

    signal.signal(signal.SIGINT, handler)
    try:
        select.select([], [], [], 1)
    except select.error:
        pass
    else:
        assert False, "select.error not raised"
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def test_select_large_fd_sets():
    import select
    import os
    import sys

    # check that select() doesn't choke on large fd sets
    # only check this if we have a getrlimit() function
    if not hasattr(os, 'getrlimit'):
        return
    # on some systems, getrlimit
