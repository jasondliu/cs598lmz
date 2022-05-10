import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    raise RuntimeError

    select.select([F()], a, a, a)


def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()

    raise RuntimeError

    select.poll()

def test_poll_small_timeout_error():
    def f():
        return 5

    select.poll(5,5)

def test_fdset_check(self):
    a = []

    class F:
        def fileno(self):
            return test_fdset_check()
            raise RuntimeError

    raise RuntimeError

    select.poll(5,5)
