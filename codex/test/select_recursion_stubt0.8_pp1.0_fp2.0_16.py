import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def close(self):
            test_select_mutated()
            pass

        def read(self):
            test_select_mutated()
            return 'read'

    rl = [F()]
    select.select(rl, [], [], 5)
    rl.append(F())

def test_select_close():
    import sys
    rl, wl, xl = select.select([sys.stdin], [], [], 5)
    del rl[:]
    del wl[:]
    del xl[:]
    sys.stdin.close()

def test_select_closed_list():
    import sys
    rl = [sys.stdin]
    del rl[0]
    rl = [sys.stdin]
    del rl[:]
    rl = [sys.stdin]
    del rl[:]
    rl.append(sys.stdin)

def test_select_closed_fd():
    import sys
    rl, wl, xl = select
