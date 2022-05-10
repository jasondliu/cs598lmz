import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    try:
        select.select([], [], [], 0)
    except ValueError:
        pass
    else:
        assert 0, "select didn't raise ValueError"

# This is a regression test for a bug in select.select() where it would
# not correctly handle a file descriptor that closed while the call was
# in progress.  The test is a bit of a hammer, but it's the best I could
# come up with.
def test_select_closed():
    import os, sys, time
    rfds, wfds, xfds = select.select([sys.stdin], [], [], 0.1)
    assert not rfds and not wfds and not xfds
    os.close(0)
    time.sleep(0.2)
    try:
        select.select([sys.stdin], [], [], 0.1)
    except ValueError:
        pass
    else:
        assert 0, "select didn't raise ValueError"

def test_select_closed
