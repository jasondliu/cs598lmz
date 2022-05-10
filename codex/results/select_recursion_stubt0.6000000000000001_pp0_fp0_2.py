import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 666

    a.append(F())
    b = select.select([], [], a, 0)
    assert b == ([], [], [])

def test_select_closed_file():
    a = []
    b = select.select([], [], a, 0)
    assert b == ([], [], [])

def test_select_closed_file_mutated():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 666

    a.append(F())
    b = select.select([], [], a, 0)
    assert b == ([], [], [])

def test_select_closed_pipe():
    r, w = os.pipe()
    try:
        os.close(w)
        a = select.select([r], [], [], 0)
        assert a == ([r], [], [])
    finally:
        os.close(r)

def test_select_closed_pipe_mutated():
    r, w = os.pipe()
   
