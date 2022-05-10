import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def close(self):
            pass

    class G:
        def fileno(self):
            a.append(1)
            return 1

        def close(self):
            pass

    f = F()
    g = G()

    select.select([f, g], [], [])
    assert a == [1]

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

        def close(self):
            pass

    f = F()

    select.select([f], [], [])
    assert a == [1]
    del a[:]
    select.select([f], [], [])
    assert a == [1]

def test_select_invalid_fds():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return -1

        def close(self):
            pass

    f = F()

    raises(ValueError, select.
