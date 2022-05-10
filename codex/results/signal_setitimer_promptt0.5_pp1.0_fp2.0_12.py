import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print "handler called"

signal.signal(signal.SIGALRM, handler)

set = signal.setitimer(signal.ITIMER_REAL, 0.001, 0.001)
print "setitimer returned", set

get = signal.getitimer(signal.ITIMER_REAL)
print "getitimer returned", get

while True:
    pass
