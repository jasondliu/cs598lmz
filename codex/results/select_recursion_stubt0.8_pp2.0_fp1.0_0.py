import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()   # zap the current frame
            return a.pop()
    x = select.select([], [], [F()]) # zap 'a'

def test_select_with_file_objects():
    a = []
    f = open(TESTFN, 'r')
    try:
        a.append(f)
        x = select.select([], [f], [])
        a[:] = range(512)
        x = select.select([], a, [])
    finally:
        a[:] = []
        f.close()
        unlink(TESTFN)

def test_select_read_only_buffer():
    try:
        buffer
    except NameError:
        return
    try:
        from _testcapi import socketpair
    except ImportError:
        return
    r, w = socketpair()
    try:
        a = buffer(b'x' * 100)
        x = select.select([r], [], [], 0.001)
        assert x == ([r], [], []), x
        os.write
