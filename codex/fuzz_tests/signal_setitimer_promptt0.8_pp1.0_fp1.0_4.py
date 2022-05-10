import signal
# Test signal.setitimer, important constants and their types.
signals = [signal.SIGALRM, signal.SIGVTALRM]
print('Testing interval timer constants...', end='')
vals = [signal.ITIMER_REAL, signal.ITIMER_VIRTUAL, signal.ITIMER_PROF]
print('ok')
for i in range(len(vals)):
    print('Testing interval timer signals and types %d/%d...' % (i + 1, len(vals)),
        end='')
    signal.setitimer(vals[i], 0, 0)
    signal.setitimer(vals[i], 0.1, 0.2)
    signal.setitimer(vals[i], 0, 0.2)
    signal.setitimer(vals[i], 0, 0)
    if vals[i] == signal.ITIMER_REAL:
        for s in signals:
            signal.signal(s, lambda n, f: None)
    print('ok')
for s in signals:
    try:
        signal.setit
