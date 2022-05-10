import signal
# Test signal.setitimer()
def time_expired():
    print('time_expired')
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, time_expired)
signal.setitimer(signal.ITIMER_REAL, 5)

signal.pause()

# Test signal.setitimer()
def time_expired():
    print('time_expired')
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, time_expired)
signal.setitimer(signal.ITIMER_REAL, 5)

signal.pause()

# Test signal.setitimer()
def time_expired():
    print('time_expired')
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, time_expired)
signal.setitimer(signal
