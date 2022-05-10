import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass
    else:
        assert False, "select() should have failed"

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
    except ValueError:
        pass
    else:
        assert False, "select() should have failed"

def test_select_closed_pipe():
    import os
    import sys
    import errno

    r, w = os.pipe()
    try:
        os.close(w)
        try:
            select.select([r], [], [], 0)
        except select.error as e:
            assert e.args[0] == errno.EBADF
        else:
            assert False, "select() should have failed"
    finally:
        os.close(r)

