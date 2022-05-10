import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    if sys.platform in ('win32', 'riscos'):
        f = F()
        try:
            select.select([f], [], [])
        except ValueError:
            a.append(sys.exc_info()[1])
        a[0] = a[0].args[0]
        efilt = a[0]
        expected = [errno.EBADF, errno.WSAENOTSOCK]
    else:
        f = 42
        try:
            select.select([f], [], [])
        except ValueError:
            a.append(sys.exc_info()[1])
        a[0] = a[0].args[0]
        efilt = a[0]
        expected = 'Bad file descriptor'

    if not hasattr(errno, 'EBADF'):
        expected = getattr(errno, 'EBADF')

    try:
        select.select([f], [], [])
    except ValueError:
        a.append(sys.exc_info()[1])

