import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])

def test_select_bad_fd():
    class BadFD:
        def fileno(self):
            return None
    select.select([BadFD()], [], [])

def test_select_no_fileno():
    class NoFileno(object):
        pass
    select.select([NoFileno()], [], [])

def test_select_close_fd_on_error():
    error = None

    class BadFD:
        def fileno(self):
            raise ValueError()

    fd = os.open(test.support.TESTFN, os.O_CREAT)
    try:
        try:
            select.select([BadFD()], [fd], [])
        except ValueError:
            error = sys.exc_info()[1]
        else:
            self.fail("Expected ValueError")
    finally:
        os.close(fd)
        if error:
            raise error
