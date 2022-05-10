import signal
# Test signal.setitimer() with alarm, interval and ITIMER_REAL

from test.support import verbose
if os.name == 'posix':
    if verbose:
        print('There will be output for every signal caught.')
    realtime = signal.ITIMER_REAL
    alarm = 0.2
    interval = 0.1

    # Print how many signals we've caught so far.
    signals_catched = 0
    def handler(signum, frame):
        global signals_catched
        signals_catched += 1
        print('Signal', signum, 'caught. Catching signal:', signals_catched)

    signal.signal(signal.SIGALRM, handler)

    signal.setitimer(realtime, alarm, interval)

    # Wait two seconds before killing the test.  It should have printed at
    # least one signal already.
    time.sleep(2)
    signal.setitimer(realtime, 0, 0)
    if signals_catched == 0:
        if verbose:
            print('***Test seems broken***')
