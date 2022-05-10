import signal
# Test signal.setitimer()

def handler(*args):
    print "Got", args

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

for i in range(3):
    print "Sleeping", i
    time.sleep(1)

signal.setitimer(signal.ITIMER_REAL, 0, 0)

print "Done"
