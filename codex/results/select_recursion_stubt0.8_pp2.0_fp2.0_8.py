import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

        def read(self):
            a.append(1)

    select.select([F()], [], [], 1)

def test_select_unhashable():
    class F:
        def fileno(self):
            return 1
    select.select([F()], [], [], 1)

def test_select_dereferencing():
    class F:
        def fileno(self):
            return 1
        def __del__(self):
            raise RuntimeError

    f = F()
    select.select([f], [], [], 1)
    f = None

def limiter(size):
    def limiter_generator():
        for i in xrange(size):
            yield i
    return limiter_generator()

def test_file_read_limited():
    # Issue #20031
    # Test that read() methods don't read past the size specified
    # by the user, even if they could.
    f = tempfile.TemporaryFile()
    try:
        f.write(b'x
