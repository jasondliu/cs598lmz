import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [])
    select.select([F()], [], [], 0)
    select.select([], [F()], [], 0)
    select.select([], [], [F()], 0)

def test_threeway_findfile_mutated_by_open():
    class F:
        def seekable(self):
            return True
        def tell(self):
            return 0

    a = [F(), open(__file__, "rb")]
    select.select([], [], [], 0)
    import gc
    gc.collect() # this used to crash

def test_badtimer():
    import select
    t = select.epoll.timer()
    try:
        t.cance()
    except:
        pass
