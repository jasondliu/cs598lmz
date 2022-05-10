import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)


def test_select_bad_fds():
    class FileLike:
        def fileno(self):
            return 'this should not be allowed'

    try:
        select.select([FileLike()], [], [])
    except TypeError as e:
        assert str(e) == 'fileno() returned a non-integer (type str)'
    else:
        raise AssertionError('TypeError not raised')


def test_select_bad_list():
    try:
        select.select(1, 2, 3)
    except TypeError as e:
        assert str(e) == 'arguments must be lists or tuples'
    else:
        raise AssertionError('TypeError not raised')


def test_select_bad_timeout():
    try:
        select.select([], [], [], 'foo')
    except TypeError as e:
        assert str(e) == 'timeout must be a float or None'
