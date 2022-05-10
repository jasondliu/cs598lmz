import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    class G:
        def fileno(self):
            return a.pop()

    a = [F(), G()]
    select.select([], [], [])

def test_select_error():
    import select
    import errno
    import os

    # Issue #14078: select.select() should raise an exception when the
    # list of fds is mutated by another thread.
    class MutatingList(list):
        def __getitem__(self, index):
            if index == 0:
                del self[:]
            return list.__getitem__(self, index)

    fd = os.open(__file__, os.O_RDONLY)
    try:
        l = [fd]
        select.select(MutatingList(l), [], [], 0.1)
    except select.error as e:
        assert e.args[0] == errno.EINVAL
    else:
        assert False, "Expected select.error"
    finally:
        os.close(fd)
