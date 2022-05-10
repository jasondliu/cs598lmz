import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 3

        def readable(self):
            return True

    f = F()
    select.select([f], [], [])
    f.__dict__.update(f.__dict__)
    select.select([f], [], [])
    assert a == [f, f]

def test_kevent_mutated():
    a = []

    class F:
        def fileno(self):
            test_kevent_mutated()
            a.append(self)
            return 3

        def readable(self):
            return True

    f = F()
    select.kqueue().control([select.kevent(f, select.KQ_FILTER_READ)], 0, 0)
    f.__dict__.update(f.__dict__)
    select.kqueue().control([select.kevent(f, select.KQ_FILTER_READ)], 0, 0)
    assert a == [f, f]
