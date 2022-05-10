import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 100

        def close(self):
            a.append(1)

    select.select([F()], [F()], [F()])
    assert a == [1, 1, 1]

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(r)
    os.close(w)
    res = select.select([r], [], [], 0)
    assert res == ([], [], []), res

def test_select_closed_pipe_2():
    r, w = os.pipe()
    os.close(r)
    os.close(w)
    res = select.select([r], [], [], 0)
    assert res == ([], [], []), res

def test_select_closed_pipe_3():
    r, w = os.pipe()
    os.close(w)
    os.close(r)
    res = select.select([], [w], [], 0)
    assert res == ([], [], []), res


