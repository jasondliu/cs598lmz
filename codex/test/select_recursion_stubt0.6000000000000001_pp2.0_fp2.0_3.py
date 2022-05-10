import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # recurse
            return 0

        def close(self):
            a.append(1)

    old_alarm = signal.signal(signal.SIGALRM, lambda n,f: sys.exit())
    signal.alarm(1)
    try:
        select.select([F()], [], [])
    except SystemExit:
        pass
    assert a == [1]
    signal.signal(signal.SIGALRM, old_alarm)
    signal.alarm(0)

def test_select_interrupted():
    a = []

    class F:
        def fileno(self):
            test_select_interrupted() # recurse
            return 0

        def close(self):
            a.append(1)

    old_alarm = signal.signal(signal.SIGALRM, lambda n,f: sys.exit())
    signal.alarm(1)
    try:
        select.select([F()], [], [])
    except SystemExit:
        pass
    assert a == [1]
    signal
