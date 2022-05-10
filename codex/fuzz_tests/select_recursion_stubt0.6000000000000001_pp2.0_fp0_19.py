import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    class C:
        def __getitem__(self, i):
            a.append(i)
            return i
        def __len__(self):
            return 3

    select.select(C(), [], [])
    assert a == [0, 1, 2]

def test_select_list():
    import sys
    if sys.platform == 'win32':
        skip('only works on posix')
    r, w, x = select.select([sys.stdin], [], [], 0)
    assert r == []

def test_select_timeout():
    import sys
    if sys.platform == 'win32':
        skip('only works on posix')
    r, w, x = select.select([sys.stdin], [], [], 0)
    assert r == []
    r, w, x = select.select([sys.stdin], [], [], 0.5)
    assert r == []

def test_select_closed_pipe():
    import sys
    if sys.platform == 'win32':
       
