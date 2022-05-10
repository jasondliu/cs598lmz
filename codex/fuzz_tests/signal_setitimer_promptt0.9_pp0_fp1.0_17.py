import signal
# Test signal.setitimer, signal.getitimer, signal.ITIMER_REAL, signal.ITIMER_VIRTUAL,
# signal.ITIMER_PROF

import sys

signal_timed_out = False

def handler(signum, frame):
    global signal_timed_out
    if signum == signal.SIGALRM:
        print("SIGALRM!")
        signal_timed_out = True


# schedule an alarm after half a second with resolution 1/10 second
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.1)
# get it back to probe if it actually worked
tv = signal.getitimer(signal.ITIMER_REAL)
if tv == (0.0, 0.1):
    # XXX: This will always pass, as tv is a tuple. We need a way
    # to compare tuples in PyPy, and allow them in PyPy's RPython
    # code...
    pass

#
