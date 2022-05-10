import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([EINTR], a, a)
    select.select([], [EINTR], [EINTR], -1)
    select.select([], a, a, -1)
    try:
        select.select([EINTR], a, a, -1)
    except:
        pass
    select.select([], [EINTR], a, -1)
    try:
        select.select([F()], a, a, -1)
    except:
        pass

def test_wait_mutated():
    Ready = []

    class P:
        def poll(self):
            exit(0)

    os.wait([EINTR])
    os.wait()
    os.wait(Ready)
    try:
        os.wait(EINTR)
    except:
        pass
    try:
        os.wait(P())
    except:
        pass

def test_wait_mutated():
    Ready = []

    class P:
        def poll(self):
            exit(
