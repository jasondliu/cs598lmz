import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
        def read(self): pass
        
    f = F()

    try:
        select.select([f], a, a)
    except RuntimeError:
        pass
    else:
        raise AssertionError, "select did not restart in case of mutation"

def test_select_raise():
    class F:
        def fileno(self): return 1
        def read(self): raise ValueError
        
    f = F()
    # just check if this raises anything
    select.select([f], [], [])

def test_pipe():
    rnum = 666
    p1, p2 = os.pipe()
    fd = os.open('/dev/null', os.O_WRONLY)
    try:
        for i in range(200):
            os.write(p1, 'x' * rnum)
            s = os.read(p2, rnum)
            assert len(s) == rnum
            # if the underlying system supports it, check if the other end of
            # the pipe is still full

