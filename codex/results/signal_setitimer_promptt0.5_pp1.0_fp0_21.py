import signal
# Test signal.setitimer()
# 
# 1. signal.setitimer()
# 2. signal.getitimer()

def signal_handler(signum, frame):
    print "signal_handler: signal num {}".format(signum)

def signal_handler_1(signum, frame):
    print "signal_handler_1: signal num {}".format(signum)

def signal_handler_2(signum, frame):
    print "signal_handler_2: signal num {}".format(signum)

signal.signal(signal.SIGALRM, signal_handler)
signal.signal(signal.SIGVTALRM, signal_handler_1)
signal.signal(signal.SIGPROF, signal_handler_2)

print signal.getitimer(signal.ITIMER_REAL)
signal.setitimer(signal.ITIMER_REAL, 2, 0)
print signal.getitimer(signal.ITIMER_REAL)

signal.setitimer(signal.
