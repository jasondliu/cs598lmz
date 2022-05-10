import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    f = F()
    a.append(f)
    try:
        select.select(a, a, a, 0)
    except ValueError:
        pass
    a.remove(f)
    select.select(a, a, a, 0)

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return 0
    f = F()
    a.append(f)
    fd = f.fileno()
    os.close(fd)
    try:
        select.select(a, a, a, 0)
    except ValueError:
        pass
    a.remove(f)
    select.select(a, a, a, 0)

def test_select_closed_pipe():
    r, w = os.pipe()
    try:
        os.close(w)
        select.select([r], [], [], 0)
    finally:
        os.close(r)

