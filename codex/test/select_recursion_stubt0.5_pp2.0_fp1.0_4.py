import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

    a.append(F())

    try:
        select.select([], [], a, 1)
    except:
        pass

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 5

    a.append(F())

    try:
        select.select([], [], a, 1)
    except:
        pass

def test_select_closed_pipe():
    # This is a test for a bug in select.select() on Mac OS X.
    # The bug is that select.select() doesn't raise an exception
    # if the read end of a pipe is closed.  Instead, it reports
    # that the file descriptor is ready for reading.  This is
    # incorrect.

    import os

    # Create a pipe.
    r, w = os.pipe()

    # Close the read end of the pipe.
    os.close(r)

    # Wait for the write end of the pipe to become ready for writing.
    # This will never happen because the other end of the pipe
