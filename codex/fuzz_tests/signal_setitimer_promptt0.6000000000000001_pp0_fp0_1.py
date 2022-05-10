import signal
# Test signal.setitimer()

def handler(sig, frame):
    print "Got signal", sig

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    signal.pause()
