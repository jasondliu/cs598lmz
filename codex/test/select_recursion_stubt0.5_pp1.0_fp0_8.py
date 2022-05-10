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
