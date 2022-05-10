import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    select.select([F()], [], [])

def test_select_add():
    def make_pipe():
        r, w = os.pipe()
        return r, w, os.fdopen(r, 'rb', 0), os.fdopen(w, 'wb', 0)

    def make_sock():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 0))
        s.listen(1)
        return s

    rp, wp, rf, wf = make_pipe()
    rs, ws = make_sock()

    for i in range(15):
        ra, wa, xa = select.select([rp], [wp], [])
        assert not ra and wa
        select.select([rs], [], [])
        ra, wa, xa = select.select([rp], [wp], [])
        assert not ra and wa
        select.select([], [ws],
