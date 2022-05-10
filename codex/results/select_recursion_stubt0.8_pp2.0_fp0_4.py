import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 4
    f = F()
    fd = [f]
    test_select_mutated()
    try:
        select.select(fd, fd, fd, 0)
    finally:
        test_select_mutated()
        fd.remove(f)
    test_select_mutated()
    return len(a) > 0

def test_select_mutated_multiple():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 4
    f = F()
    fd = [f]
    try:
        select.select(fd, fd, fd, 0)
    finally:
        fd.remove(f)
    return test_select_mutated()

def test_select_mutated_with_remove():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 4
    f = F()
    fd = [f]
    select
