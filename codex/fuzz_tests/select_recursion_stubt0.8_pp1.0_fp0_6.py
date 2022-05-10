import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    s = select.select([F()], a, a)

    assert s == ((), [], [])

def test_select_interrupted():
    import os, signal
    for sig in [signal.SIGALRM, signal.SIGUSR1]:
        oldsig = signal.signal(sig, signal.SIG_IGN)
        try:
            raises(select.error, select.select, [], [], [], 1)
        finally:
            signal.signal(sig, oldsig)

def test_select_FD_CLOEXEC_leak():
    fds = []
    for i in range(130):
        fds.append(os.open(__file__, os.O_RDONLY))
    l = select.select(fds, [], [])
    for fd in fds:
        os.close(fd)
