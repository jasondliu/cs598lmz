import signal
# Test signal.setitimer
# The system must be able to set the status of the timer to ITIMER_REAL
# and ITIMER_VIRTUAL
# The ITIMER_REAL timer status is tested by signal.setitimer and then by
# the process being killed by signal.SIGALRM
# The ITIMER_VIRTUAL timer status is tested by signal.setitimer and then by
# the process being killed by signal.SIGVTALRM

def handler(signum, frame):
    print("Handler called for signum", signum)
    signal.setitimer(signal.ITIMER_REAL, 0.0, 0.0)
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.0, 0.0)
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)
signal.setit
