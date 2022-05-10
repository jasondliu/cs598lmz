import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

print "Starting..."
while delays:
    for i in range(1,N):
        pass
    # select.select([], [], []) - would do the same -- sleep.
    # os.system("./dummy") -- a simple process is far slower than that little loop.
print "Done."
