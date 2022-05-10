import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(w)
    select.select([r], [], [], 0)

def test_select_closed_pipe_2():
    r, w = os.pipe()
    os.close(r)
    select.select([w], [], [], 0)

def test_select_closed_pipe_3():
    r, w = os.pipe()
    os.close(w)
    os.close(r)
    select.select([w], [], [], 0)

def test_select_closed_pipe_4():
    r, w = os.pipe()
    os.close(r)
    os.close(w)
