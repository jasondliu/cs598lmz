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

def test_select_large_fd():
    try:
        select.select([0x80000000], [], [])
    except ValueError:
        pass
    else:
        raise Exception("should have raised ValueError")
