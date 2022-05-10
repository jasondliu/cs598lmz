import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def select(self, iwtd, owtd, ewtd, timeout=None):
            a.append(1)
            return 1, 0, 0

    select.select([F()], [], [], 1)
    assert a == [1]

def test_select_no_fileno():
    class F:
        def select(self, iwtd, owtd, ewtd, timeout=None):
            return 1, 0, 0

    raises(AttributeError, select.select, [F()], [], [], 1)

def test_select_strange_fd():
    from select import epoll

    class F:
        def fileno(self):
            return -1

        def select(self, iwtd, owtd, ewtd, timeout=None):
            return 1, 0, 0

    select.select([F()], [], [], 1)
    assert epoll.EPOLL_CLOEXEC == 0

def test_select_bad_select():
    import errno
    from select import poll

   
