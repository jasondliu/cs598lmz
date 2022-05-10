import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    for i in range(10):
        status = errno.EIO
        try:
            select.select([F()], a, a, 0.1)
        except select.error as e:
            if e.args[0] != errno.EIO:
                raise AssertionError("Unexpected errno %s, expected %s" %
                                     (e.args[0], errno.EIO))


class ExpectError(Exception):
    pass

def f():
    pass

def test_select_filedescriptor_closed():
    fd = f.__code__.co_firstlineno
    try:
        for i, r in enumerate(range(select.PIPE_BUF + 3)):
            os.close(fd + i)
        select.select([fd], [fd], [fd], 0)
    except OSError:
        raise ExpectError
    else:
        raise AssertionError("Unexpectedly succeeded")


