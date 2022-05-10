import signal
# Test signal.setitimer(signal.ITIMER_REAL, 0, 0)

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise SystemExit('Exiting')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

# Test signal.setitimer(signal.ITIMER_REAL, 0.02, 0.01)

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise SystemExit('Exiting')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.02, 0.01)

# Test signal.setitimer(signal.ITIMER_REAL, 0.02, 0.01)

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise SystemExit('Exiting')


