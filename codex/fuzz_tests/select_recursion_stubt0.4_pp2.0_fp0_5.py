import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    a.append(F())

    try:
        select.select([], [], [a[0]])
    except IndexError:
        pass
    else:
        assert False, 'did not raise IndexError'

def test_select_error():
    import select
    import errno

    a = []

    class F:
        def fileno(self):
            return len(a)
    a.append(F())

    try:
        select.select([], [], [a[0]])
    except OSError as e:
        assert e.errno == errno.EBADF
    else:
        assert False, 'did not raise OSError'

def test_select_error_2():
    import select
    import errno

    a = []

    class F:
        def fileno(self):
            return len(a)
    a.append(F())

    try:
        select.select([], [a[0]], [])
    except OSError as e:
       
