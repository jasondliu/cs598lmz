import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
    r, w, x = select.select([F()], [F()], [F(), s], 0)
    del a, r, w, x, s
    gc.collect()
    gc.collect()
    gc.collect()

def test_select_mutated_dummy():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_dummy()
            return 42

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
    dummy_r = []
    dummy_w = []
    dummy_x = []
    r, w, x = select.select([F(), s], dummy_w, dummy_x, 0)
    del a, r, w, x, s, dummy_r, dummy_w, dummy_x
    gc.collect()
    g
