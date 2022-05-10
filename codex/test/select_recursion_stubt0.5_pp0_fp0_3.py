import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    select.select([], [], a)
    a.append(F())
    select.select([], [], a)

def test_select_large_fd():
    # Issue #12757
    # select should not crash when a file descriptor >= FD_SETSIZE is passed
    # to select().
    try:
        select.select([], [], [], 0, 1)
    except ValueError:
        pass

# Issue #15751
def test_select_bad_timeout():
    # select should not crash when a negative timeout is passed
    try:
        select.select([], [], [], -1)
    except ValueError:
        pass

def test_select_large_timeout():
    # Issue #16500
    # select should not crash when a timeout >= 2**31 is passed
    try:
        select.select([], [], [], 2**31)
    except OverflowError:
        pass

