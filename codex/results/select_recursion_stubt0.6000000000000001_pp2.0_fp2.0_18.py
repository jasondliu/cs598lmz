import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # mutate list
            return 0
    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [], 0)
    except OSError:
        pass
    os.close(r)

def test_select_bad_descriptor():
    try:
        select.select([-1], [], [], 0)
    except ValueError:
        pass
    try:
        select.select([100000], [], [], 0)
    except ValueError:
        pass

def test_select_unhashable():
    try:
        select.select([[1,2]], [], [], 0)
    except TypeError:
        pass

def test_select_unhashable_fileno():
    class UnhashableWithFileno:
        def fileno(self
