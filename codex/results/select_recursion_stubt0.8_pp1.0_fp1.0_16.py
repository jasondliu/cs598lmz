import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() #ouch
            return 1
        def read(self):
            raise EOFError

    f = F()
    # We would like to check that we didn't select a closed file
    # descriptor, so we check *before* writing to the socket.
    a.append(id(select.select([f],[],[],0)))
    # But some platforms select on closed fds, so we may have to
    # continue with the check *after* writing to the socket.  If the
    # check succeeds then, it is likely that the check above succeeded
    # too.
    a.append(id(select.select([f],[],[],0)))
    sys.stdout.write('.')

def test_select_bad_file():
    # Test that select() on a bad file descriptor raises EBADF.
    # See bug #1079662.
    try:
        os.closerange(1000, 3000)
    except OSError:
        pass
    else:
        # The test will still pass, but we print a warning just in case.
        # If you see the warning and
