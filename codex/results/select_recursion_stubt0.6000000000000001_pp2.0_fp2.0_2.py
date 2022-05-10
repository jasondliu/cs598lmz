import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
        def __del__(self):
            a.append(1)

    select.select([F()], [], [], 0)
    del a[:]
    res = select.select([F()], [], [], 0)
    assert res == ([], [], []), res
    assert a == [1], a

def test_select_del():
    a = []

    class F:
        def fileno(self):
            return 0
        def __del__(self):
            a.append(1)

    select.select([F()], [], [], 0)
    del a[:]
    res = select.select([F()], [], [], 0)
    assert res == ([], [], []), res
    assert a == [1], a

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return 0
        def __del__(self):
            a.append(1)

    p = select.poll()
   
