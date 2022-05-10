import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Got signal", signum

signal.signal(signal.SIGALRM, handler)

# setitimer() takes 3 arguments:
# which timer to set,
# how long until the first signal,
# how often to send the signal

signal.setitimer(signal.ITIMER_REAL, 1, 1)

while 1:
    pass
