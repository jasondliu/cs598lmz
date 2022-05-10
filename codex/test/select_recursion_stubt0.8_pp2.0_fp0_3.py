import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # crash
            return 10
    f = F()
    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_select_wait():
    import time
    import thread, threading

    def add_input(l, inp):
        # give it a bit of time to start select
        time.sleep(0.1)
        # hold the lock while adding the input
        l.acquire()
        try:
            inp.append(None)
        finally:
            l.release()

    for i in xrange(10):
        l = threading.Lock()
        l.acquire()
        inp = []
        thread.start_new_thread(add_input, (l, inp))
        ready, out, exc = select.select([inp], [], [])
