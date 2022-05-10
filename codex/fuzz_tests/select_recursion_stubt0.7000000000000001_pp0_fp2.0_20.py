import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    select.select([F(), F()], [], [])

def test_select_keyboardinterrupt():
    import os, time
    fd = os.open(__file__, os.O_RDONLY)
    try:
        select.select([fd], [], [], 0.01)
    except KeyboardInterrupt:
        pass

def test_select_except():
    import errno
    try:
        select.select([], [], [], -1)
    except OSError as e:
        assert e.args[0] == errno.EINVAL
    else:
        assert False, "didn't raise"

class TestException(Exception):
    pass

def test_select_interrupted_error():
    import os, time, errno

    fd = os.open(__file__, os.O_RDONLY)
    try:
        select.select([fd], [], [], 0.01)
    except TestException:
        pass

def test_select_interrupted_noerror
