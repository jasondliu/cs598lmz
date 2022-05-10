import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def do_select():
        select.select([F()], [], [])

    a.append(1)
    do_select()
    a.append(2)
    do_select()
    a.append(3)
    do_select()

def test_select_large_fd():
    # Issue #5679: select() should not raise an OverflowError when given
    # a large file descriptor.
    try:
        select.select([fd], [], [], 0)
    except OSError as e:
        if e.errno == errno.EBADF:
            # This is expected on Windows.
            pass
        else:
            raise

def test_select_large_list():
    # Issue #10741: select() should not raise an OverflowError when given
    # a large list.
    try:
        select.select(list(range(sys.maxsize)), [], [], 0)
    except OSError as e:
        if e.errno == errno.EBADF
