import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])
    a.append(1)

# The following test does not work on Windows, because it
# uses a select loop to test for the blocking feature.
# It's not difficult to add it, but it's not worth the
# effort.
if sys.platform != 'win32':
    def test_select_blocking():
        # Issue #10100: select() should not block if all file descriptors are
        # non-blocking.
        fd = os.open(os.devnull, os.O_RDONLY | os.O_NONBLOCK)
        try:
            select.select([fd], [], [], 0.0)
        finally:
            os.close(fd)

def test_select_error():
    # Issue #10357: select() failed with a file descriptor larger than FD_SETSIZE
    # even if it was not passed to select().

    # Sanity check: select() with an empty list should not fail.
    select.select([], [], [])

    # Create a
