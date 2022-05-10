import signal
# Test signal.setitimer() and signal.getitimer() methods.
# This also tests the SA_RESTART behaviour - see the code.
# This works by sending itself SIGALRM after a delay, and checking
# that the time value is reset to the original interval.

def handler(signum, frame):
    value = signal.getitimer(signal.ITIMER_REAL)
    if value != [5, 0.0]:
        print("FAILED: returned", value)
        sys.exit(1)
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)

value = signal.setitimer(signal.ITIMER_REAL, 5, 1)
if value != [0, 0.0]:
    print("FAILED: returned", value)
