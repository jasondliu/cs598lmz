import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    s = select.select([F()], a, a)
    s[0][0].fileno()

def test_select_closed_fileno():
    class Foo:
        def fileno(self):
            return 1
    f = Foo()

    # Close the file descriptor returned by f.fileno().
    #
    # According to http://docs.python.org/library/select.html#select.poll
    # "The argument to close() can be, and usually is, different from the
    # file descriptor returned by fileno()."
    #
    # On Windows, this would raise "ValueError: [Errno 9] Bad file
    # descriptor", which is not what we want.  We want the poll() or
    # select() call to raise a "Bad file descriptor" error.
    os.close(f.fileno())

    # The "select" module is supposed to raise a "Bad file descriptor" error
    # if any of the arguments to select() have a file descriptor that has
    # been closed.
    #
    #
