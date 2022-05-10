import signal
# Test signal.setitimer
def handler(signum, frame):
    print("Alarm")
    signal.setitimer(signal.ITIMER_REAL, 0)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)

# Test signal.getsignal
def handler(signum, frame):
    print("Alarm")
    signal.setitimer(signal.ITIMER_REAL, 0)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)

# Test signal.signal
def handler(signum, frame):
    print("Alarm")
    signal.setitimer(signal.ITIMER_REAL, 0)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)

# Test signal.getsign
