import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGALRM, handler)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGALRM, handler)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGALRM, handler)

# Test signal.setitimer()
