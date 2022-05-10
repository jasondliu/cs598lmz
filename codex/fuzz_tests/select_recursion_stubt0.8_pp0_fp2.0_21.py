import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return -1

    r = select.select([F()], [], [], 1)
    if len(r) != 0 or a != []:
        print(r, a)
        raise RuntimeError

def test_select_largefd():
    maxfd = select.__fd_needs_raising__
    if maxfd is not None:
        maxfd = maxfd.max
    if maxfd is not None and maxfd + 1 > select.FD_SETSIZE:
        try:
            select.select([maxfd], [], [])
        except ValueError:
            pass
        else:
            print("supported fd too large")
            raise RuntimeError
    else:
        try:
            select.select([maxfd + 1], [], [])
        except ValueError:
            pass
        else:
            print("supported fd too large")
            raise RuntimeError

def test_select_largefd_list():
    maxfd = select.__fd_needs_raising__
    if maxfd is not None:
        maxfd
