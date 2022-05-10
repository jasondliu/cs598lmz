import signal
# Test signal.setitimer and signal.getitimer

def handler(signum, frame):
    pass

signal.signal(signal.SIGALRM, handler)

it = signal.ITIMER_REAL
# signal.setitimer(it, 0.1, 0.1)

signal.setitimer(it, 0.01, 0.01)
signal.getitimer(it)

# signal.setitimer(it, 0.2, 0.2)
signal.setitimer(it, 0.02, 0.02)
signal.getitimer(it)

signal.setitimer(it, 1.0, 1.0)
signal.getitimer(it)
# itimers do not accurately deliver the asked-for times

