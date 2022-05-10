import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [F()], [F()], 0.1)
    # ^ this used to crash because the list of fds was mutated
    # by the fileno method.

def test_select_large_fd():
    # Issue #3764: select shouldn't crash with large fd (>= 2**31)
    # on 64 bits platform
    try:
        select.select([2**31], [], [], 0)
    except (ValueError, OverflowError):
        pass
    else:
        raise AssertionError("select([2**31], [], [], 0) didn't raise")
    select.select([-1], [], [], 0)

if not hasattr(select, 'epoll'):
    def test_epoll_ignored():
        pass
else:
    def test_epoll_ignored():
        # Issue #3765: select.epoll() ignored the 'sizehint' parameter
        epoll = select.epoll(1)
