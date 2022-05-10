import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return self

        def close(self):
            pass

    f = F()
    try:
        f.fileno()
    except RuntimeError:
        return

    a.append(f)
    for i in xrange(256):
        select.select([], [], [])

def test_select_exception():
    fd = os.open(test.test_support.TESTFN, os.O_WRONLY | os.O_CREAT, 0o777)
    try:
        f = open(test.test_support.TESTFN, 'rb')
        f.close()
        try:
            select.select([fd], [f], [], 10)
        except ValueError:
            pass
        else:
            raise TestFailed("ValueError not caught")
    finally:
        os.close(fd)

def test_main():
    run_unittest(__name__)

if __name__ == '__main__':
    test_main()
