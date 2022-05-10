import signal
# Test signal.setitimer with SIGALRM

def handler(signum, frame):
    print "handler"

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

print "done"
