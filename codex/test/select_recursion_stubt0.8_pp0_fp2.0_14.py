import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
    f = F()
    #
    select.select([], [], [f])
    #
    raise AssertionError


def test_none_fd():
    class F:
        def fileno(self):
            return None

    select.select([F()], [], [])


def test_negative_fd():
    class F:
        def fileno(self):
            return -10

    select.select([F()], [], [])


class BadInt:
    def __int__(self):
        raise ValueError


def test_bad_int():
    class F:
        def fileno(self):
            return BadInt()

    select.select([F()], [], [])


class BadFloat:
    def __float__(self):
        raise ValueError


def test_bad_float():
    class F:
        def fileno(self):
            return float(BadFloat())

    select.select([F()], [], [])


