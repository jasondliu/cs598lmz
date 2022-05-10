import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "timeout"
    raise Exception

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1)

try:
    while True:
        print "loop"
except:
    pass

print "done"
