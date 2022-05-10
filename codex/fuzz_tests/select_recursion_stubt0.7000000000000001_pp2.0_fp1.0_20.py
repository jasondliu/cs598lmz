import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    assert select.select([], [], a, 0) == ([], [], [])
    # must not crash
    f.fileno() == 0

def test_select_closed():
    a = []
    a.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

    class F:
        def fileno(self):
            a[0].close()
            return 0

    f = F()
    a.append(f)
    assert select.select([], [], a, 0) == ([], [], [])
    # must not crash
    f.fileno() == 0
