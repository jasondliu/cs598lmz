import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42
        def close(self):
            a.append(1)

    f = F()
    try:
        select.select([f], [], [])
    except:
        pass
    assert a == [1]
    assert f.closed


def test_select_unregister():
    import sys
    import os
    import select
    import threading
    import time

    if sys.platform == 'win32':
        # XXX: For now, skip this test on Windows.  It's possible that
        # this test could be fixed, but it's not really worth the time
        # given that this particular case is not relevant to Windows
        # users.
        return

    # Test for a bug in select.select().  On some platforms, if the
    # kernel is asked to wait for a socket that's been closed, it
    # returns immediately with that socket in the readable list.
    # This causes select() to loop forever.
    #
    # See http://bugs.python.org/issue3850 and
    # http://bugs.python.org/issue1652 for
