import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    s = select.select([F()], [], [], 0)
    assert not s[0] and not s[1] and not s[2]

def test_bad_fd():
    # Issue #20171: select.select([fd], [], [], timeout) raised a
    # ValueError if fd was an int but not a valid file descriptor.
    class FD:
        def __lt__(self, other):
            if not isinstance(other, int):
                return NotImplemented
            return self.fileno() < other
        def fileno(self):
            return -1

    select.select([2**31], [], [], 0)
    with raises(ValueError):
        select.select([-1], [], [], 0)
    with raises(ValueError):
        select.select([-2**31], [], [], 0)
    with raises(ValueError):
        select.select([FD()], [], [], 0)
    with raises(ValueError):
        select.select([object()], [
