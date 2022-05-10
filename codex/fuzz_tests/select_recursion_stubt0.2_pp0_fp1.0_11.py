import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select([], [], a)
    except RuntimeError:
        pass
    else:
        assert False, "select() didn't raise RuntimeError"

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return 0

    a.append(F())
    try:
        select.select([], [], a)
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_closed_pipe():
    import os, sys

    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [])
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"
    os.close(r)

def test_select_bad_fd():
    import os, sys

    try:
        select.select([-1], [],
