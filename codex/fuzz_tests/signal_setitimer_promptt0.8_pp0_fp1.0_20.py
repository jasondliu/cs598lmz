import signal
# Test signal.setitimer() and signal.getitimer() for SIGALRM
# and SIGPROF.

signals = [signal.SIGALRM, signal.SIGPROF]

for s in signals:
    try:
        signal.signal(s, signal.default_int_handler)
    except ValueError:
        print('skipping', s)
        continue

    signal.setitimer(s, 1, 1)
    print(signal.getitimer(s))

    while 1:
        pass
