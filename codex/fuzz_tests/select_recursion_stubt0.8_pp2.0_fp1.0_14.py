import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        r, w, x = select.select([], a, [])
    except select.error as err:
        assert err.errno == errno.EBADF
    else:
        pytest.fail("select() should have failed with EBADF")

class Data:
    """
    A class to provide an object with a readable file descriptor.
    """

    def __init__(self, data, read=True):
        """
        Create the data object with the specified source data.  Depending
        on the read argument the object will be readable or writable.
        """
        self.data = data
        self.read = read

    def fileno(self):
        """
        Return a suitable file descriptor number.
        """
        return 42

    def do_read(self, size=-1):
        """
        Read data if the object is configured to be readable.

        The size argument will be ignored and all remaining data will be
        returned.
        """
        if not self.read:
            raise Un
