import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [], [], 1)

def test_select_closed():
    class F:
        def fileno(self):
            return 5

    f = F()
    os.close(f.fileno())
    select.select([f], [], [], 1)

def test_select_closed_pipe():
    r, w = os.pipe()
    try:
        os.close(r)
        select.select([r], [], [], 1)
    finally:
        os.close(w)

def test_select_closed_pipe_2():
    r, w = os.pipe()
    try:
        os.close(w)
        select.select([r], [], [], 1)
    finally:
        os.close(r)

def test_select_closed_pipe_3():
    r, w = os.pipe()
