import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return None

    def is_readable():
        a.append(1)

    try:
        select.select([F()], [], [], 0)
        assert F().fileno() is None
    except:  # noqa
        pass

    a.append(2)

def test_select_fd_with_fileno():
    try:
        a = select.select([object()], [], [])
    except OSError as e:
        assert e.errno == 9
    else:
        assert False

    import os
    try:
        a = select.select([os.devnull], [], [])
    except OSError as e:
        assert e.errno == 9
    else:
        assert False


class RegularFile:

    def fileno(self):
        return 'abc'


