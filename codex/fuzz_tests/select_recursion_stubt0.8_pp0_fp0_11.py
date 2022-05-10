import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_select_invalid_fd():
    class F:
        def fileno(self):
            return -1
    try:
        select.select([F()], [], [])
    except ValueError:
        pass

def test_select_neg_fd():
    # Reject negative file descriptors
    with support.SuppressCrashReport():
        select.select([-1], [-1], [-1])

def test_select_bad_fd():
    # Reject non-integer file descriptors
    with support.SuppressCrashReport():
        select.select('', '', '')
