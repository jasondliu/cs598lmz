import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            # We assume that test_select_mutated() will not return
            # while we're running this test.

    a.append(F())
    select.select(a, [], [], 0.0001)

class TestFailed(Exception):
    pass

def test_select_large_fd():
    for fd in [-1, 2**31]:
        try:
            select.select([fd], [], [], 0.0001)
        except select.error as err:
            if err.args[0] != errno.EBADF:
                raise TestFailed('wrong errno for fd %i: %s' %
                                 (fd, err.args[0]))
        except ValueError:
            pass
        else:
            raise TestFailed('no error for fd %i' % fd)

def test_select_large_list():
    try:
        select.select(range(2**31), [], [], 0.0001)
    except select.error as err:
        if err.args[0] != errno.E
