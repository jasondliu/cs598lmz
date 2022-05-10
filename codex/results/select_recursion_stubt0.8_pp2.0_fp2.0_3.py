import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    select.select([f], [], [])


def test_select_closed():
    fd = os.open(test_support.TESTFN, os.O_CREAT|os.O_WRONLY)
    try:
        fd2 = os.dup(fd)
        try:
            os.close(fd)
            select.select([fd2], [], [], 0.01)
        finally:
            os.close(fd2)
    finally:
        os.remove(test_support.TESTFN)
