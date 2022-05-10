import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([F()], a, a, 0)
    assert not a

def test_select_keys():
    class F:
        def fileno(self):
            return 4
        def __str__(self):
            return 'str'
        def __repr__(self):
            return 'repr'
        def __eq__(self, other):
            return 1

    f = F()
    assert select.select([f], [f], [f], 0) == ([f], [f], [f])

def test_select_keys_closed():
    import os, sys
    if sys.platform == 'win32':
        skip("on Windows, closing a pipe end raises EBADF independently of select")
    r, w = os.pipe()
    os.close(w)
    assert os.read(r, 0) == ''
    assert select.select([r], [], [], 0) == ([r], [], [])
    os.close(r)
    raises(select.error, os.read, r, 0)
    raises(
