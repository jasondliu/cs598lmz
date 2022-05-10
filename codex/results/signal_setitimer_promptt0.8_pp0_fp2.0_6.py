import signal
# Test signal.setitimer, signal.getitimer
# For each timer, check initial value and set and get it again to second value
# and check again. Signal handler is not called.
# The timers tested are: ITIMER_REAL, ITIMER_VIRTUAL and ITIMER_PROF.

def handler(signum, frame):
    print ("timer expired")

signal.signal(signal.SIGALRM, handler)

for itimer in [signal.ITIMER_REAL, signal.ITIMER_VIRTUAL, signal.ITIMER_PROF]:
    # check initial value
    v0 = signal.getitimer(itimer)
    print ("itimer = %d: %s" % (itimer, v0))
    signal.setitimer(itimer, 0.4, 0.2)
    signal.setitimer(itimer, 0.6, 0.4)
    # check again
    v1 = signal.getitimer(itimer)
    print ("itimer = %d: %s" % (itimer, v1))
