import signal
# Test signal.setitimer()

def handler(a, b):
    print "alarm"

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)
print "sleeping"
sleep(3)
print "done"

signal.signal(signal.SIGALRM, signal.SIG_IGN)
signal.setitimer(signal.ITIMER_REAL, 1, 0)
print "sleeping"
sleep(3)
print "done"
