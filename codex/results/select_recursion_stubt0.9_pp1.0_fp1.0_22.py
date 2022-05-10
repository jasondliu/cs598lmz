import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return None
    f = F()
    b = [f]
    c = []
    r,w,x = select.select(a, b, c, 0)

def test_select_non_blocking_mutated():
    from select import select
    from socket import socketpair

    a, b = socketpair()
    r, w, x = select([a], [], [a], 0)
    a.close()
    del a
    test_select_non_blocking_mutated()

def test_iterate_non_terminating():
    class R:
        def __next__(self):
            return 37
    r = R()
    for v in r:
        pass

def test_push_to_make_space_consumed_immortal(should_crash=False):
    from _collections import deque
    def make_object():
        return deque()
    q = make_object()
    tmp = q.append
    tmp(tmp)
    tmp = tmp.__self__.appendleft
    tmp(tmp)

