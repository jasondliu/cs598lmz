import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    s = select.select([F(), F()], [], [])
    assert len(s[0]) == 2
    assert len(s[1]) == 0
    assert len(s[2]) == 0

def test_select():
    s = []
    for i in range(10):
        s.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    try:
        for i in range(len(s)):
            s[i].bind(('0.0.0.0', 0))
            s[i].listen(1)
        r, w, e = select.select(s, s, s, 1.0)
        assert len(r) == len(s)
        assert len(w) == len(s)
        assert len(e) == len(s)
        for i in range(len(s)):
            assert s[i] in r
            assert s[i] in w
            assert s[i] in e
    finally:
        for i in
