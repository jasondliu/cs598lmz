import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop(0)

    f = F()
    select.select([f], [f], [f])

test_select_mutated()

def test_fileno():
    class F: pass
    o = F()
    try:
        o.fileno()
    except AttributeError:
        pass
    else:
        assert 0, "should have raised AttributeError"

test_fileno()

def test_select():
    import select
    import time
    import sys
    import os
    import StringIO
    import os

    # we use a subprocess here, because we don't have non-blocking
    # stdio on Windows yet.
    r, w = os.pipe()
    pid = os.fork()
    if pid == 0:
        # in the child
        os.close(r)
        for i in range(5):
            # we expect this to be ready for writing, but it may
            # return either way due to timing.  The important thing is
            # that the write doesn't hang.
            select.select
