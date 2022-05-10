import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])


def test_select_large_fd():
    # Issue #16791: select() should not crash on large file descriptors.
    select.select([], [], [], 1, 1)
    select.select([], [], [], 1, 1)


def test_select_keyboard_interrupt():
    # Issue #16791: select() should not crash on large file descriptors.
    try:
        select.select([], [], [], 1, 1)
    except KeyboardInterrupt:
        pass
    select.select([], [], [], 1, 1)


def test_select_bad_fd():
    # Issue #16791: select() should not crash on large file descriptors.
    select.select([], [], [], 1, 1)
    try:
        select.select([], [], [], 1, 1)
    except OSError as e:
        assert e.errno == errno.EBADF
    else:
        assert False
