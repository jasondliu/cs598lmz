import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    try:
        select.select([F()], [], [], 0)
    except ValueError:
        pass

    assert a == []

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

        def close(self):
            a.append(2)

    try:
        select.select([F()], [], [], 0)
    except ValueError:
        pass

    assert a == [1, 2]

def test_select_regression_1():
    # regression test for https://bitbucket.org/pypy/pypy/issue/2747/
    # FileNotFoundError: [Errno 9] Bad file descriptor
    # (this happened on a test_select.py test case, which is no longer
    #  here, but we found another way to trigger the same)
    import os
    import errno
    import socket
    s = socket.socket()
    os.close(s.
