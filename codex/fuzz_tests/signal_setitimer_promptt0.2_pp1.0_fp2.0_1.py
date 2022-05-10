import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Signal handler called with signal", signum

signal.signal(signal.SIGALRM, handler)

# This call sets an alarm to go off in 2 seconds
signal.setitimer(signal.ITIMER_REAL, 2)

print "Before the sleep"
time.sleep(4)
print "After the sleep"
