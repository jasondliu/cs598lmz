import signal
# Test signal.setitimer on a signal not in the "safe" set.
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
# Test signal.setitimer on a signal in the "safe" set.
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2, signal.SIGALRM)

# Test that an alarm is triggered on a signal not in the "safe" set.
def handler(signum, frame):
    print('Signal', signum, 'received')
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

# Test that an alarm is triggered on a signal in the "safe" set.
def handler(signum, frame):
    print('Signal', signum, 'received')
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2
