import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])
    select.select([], [F()], [])
    select.select([], [], [F()])
    select.select([F()], [F()], [F()])

def test_select_mutated_epoll():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_epoll()
            return 0

    select.epoll().register(F(), select.EPOLLIN)
    select.epoll().register(F(), select.EPOLLOUT)
    select.epoll().register(F(), select.EPOLLIN | select.EPOLLOUT)

def test_select_mutated_kqueue():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_kqueue()
            return 0

    select.kqueue().control([select.kevent(F(), select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0)
   
