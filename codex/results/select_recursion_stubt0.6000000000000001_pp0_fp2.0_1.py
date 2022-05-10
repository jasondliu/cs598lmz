import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    a.append(F())
    try:
        select.select(a, [], [])
    except ValueError:
        pass

def test_select_closed_fd():
    import os, select

    fd = os.open(__file__, os.O_RDONLY)
    try:
        select.select([fd], [], [])
    finally:
        os.close(fd)

def test_select_large_fd():
    import os, select

    try:
        maxint = sys.maxint
    except AttributeError:
        maxint = sys.maxsize

    select.select([maxint], [], [])
    select.select([maxint+1], [], [])
    select.select([maxint+2], [], [])

def test_select_large_list():
    import select
    select.select(list(range(sys.maxsize)), [], [])
    select.select([], list(range(sys.maxsize)), [])
    select.select([], [], list(
