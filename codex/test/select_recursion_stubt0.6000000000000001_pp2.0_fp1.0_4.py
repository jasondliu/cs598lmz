import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    fds = [F(), F()]
    try:
        select.select([fds[0]], [], [])
    except IndexError:
        pass
    else:
        raise AssertionError

def test_select_closed_pipe():
    reader, writer = os.pipe()
    os.close(reader)
    try:
        r, w, x = select.select([reader], [], [], timeout=0.1)
    except OSError:
        pass
    else:
        raise AssertionError

def test_select_negative_fd():
    # This test is only meaningful when the underlying select()
    # call actually uses a signed integer for the file descriptor.
    # This is the case on Windows.
    reader, writer = os.pipe()
    try:
        r, w, x = select.select([reader], [], [], timeout=0.1)
    except OSError:
        pass
    else:
        raise AssertionError
    os.close(reader)
   
