import signal
# Test signal.setitimer
#
# This test may fail on systems that don't support setitimer
# (e.g. Windows) or where the clock resolution is too coarse
# (e.g. Hurd).

def handler(signum, frame):
    print("handler")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.001, 0)

while True:
    pass
