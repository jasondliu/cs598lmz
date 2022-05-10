import signal
# Test signal.setitimer
# This program should print "hello" three times,
# then exit silently.

def handler(signum, frame):
    print "hello"

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass
