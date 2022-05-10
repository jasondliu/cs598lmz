import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    try:
        select.select([F()], [], [], 0.0)
    except:
        a.append(sys.exc_info())

    check_str_exception(a[0], KeyError, "Bad file descriptor")
