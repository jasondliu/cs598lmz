import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return f.fileno()

    f = F()
    a.append(f)
    select.select([f], [], [])

if sys.platform[:3] != 'win':
    # The regression check tests that poll.poll modifies poll object
    # even if select was interrupted earlier by a signal.

    import pickle

    try:
        import os
        import signal
        import _thread
        import select

        _pollinst = select.poll()
        _interrupted = 0

        _pollcount = 0

        def _interrupt():
            global _interrupted

            _interrupted = 1
            _thread.interrupt_main()

        def _countpoll():
            _pollcount = 0
            _pollinst.register(signal.SIGALRM, select.POLLIN)
            old_handler = signal.signal(signal.SIGALRM, _interrupt)
            try:
                signal.alarm(1)
                while not _interrupted:
                    _pollcount += 1
                    r = _pollinst.poll()
            finally:
               
