import signal
# Test signal.setitimer
INITIAL_TIME = 1
INTERVAL_TIME = 2


def handler(num, stack):
    print "Signal handler called with signal", num
    signal.setitimer(signal.ITIMER_REAL, 0)
    signal.setitimer(signal.ITIMER_REAL, INITIAL_TIME, INTERVAL_TIME)


signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, INITIAL_TIME, INTERVAL_TIME)

for i in range(5):
    print "loop:", i
    signal.pause()

# Test signal.setitimer exception
