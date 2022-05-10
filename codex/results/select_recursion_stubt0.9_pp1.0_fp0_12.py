import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [])

try:
    select.kqueue()
except AttributeError:
    pass
else:
    def test_kevent_buf_len():
        kqueue = select.kqueue()
        ev = select.kevent(1, select.KQ_FILTER_READ, select.KQ_EV_ADD)
        try:
            kqueue.control([ev], 0, 1)
        finally:
            kqueue.close()

    def test_kevent_free():
        a = []

        class F:
            def fileno(self):
                a.append(1)
                return 3

        kqueue = select.kqueue()
        try:
            ev = select.kevent(1, select.KQ_FILTER_READ, select.KQ_EV_ADD)
            res = kqueue.control([ev], 0, 0)
            if res == []:
                raise unittest.SkipTest("unable to test, kqueue appears to be empty")
            del
