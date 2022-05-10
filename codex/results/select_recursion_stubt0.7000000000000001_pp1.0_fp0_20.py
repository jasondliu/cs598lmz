import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def close(self):
            a.append(1)

    select.select([F()], [], [])

def test_regression_1050800():
    import errno
    L = []
    try:
        select.select(L, L, L, 0)
    except ValueError as msg:
        assert str(msg) == "filedescriptor out of range in select()"
    else:
        assert 0, "select() failed to detect an invalid file descriptor."
    try:
        select.select(L, L, L, None)
    except ValueError as msg:
        assert str(msg) == "filedescriptor out of range in select()"
    else:
        assert 0, "select() failed to detect an invalid file descriptor."

def test_select_large_fd():
    import os
    import sys
    import errno
    # try to create a file with a large enough file descriptor
    # to cause overflow in various internal calculations
    fd = os.dup(1)
    try:
        os.close(fd
