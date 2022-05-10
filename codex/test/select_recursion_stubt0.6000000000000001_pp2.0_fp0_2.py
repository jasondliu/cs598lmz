import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 2
    f = F()
    a.append(f)
    fd = f.fileno()
    if fd != 2:
        raise test_support.TestFailed("fileno() returned %d, instead of 2" % fd)

