import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def update():
    print u'\u001B[1A\u001B[2K',
    print "%.6f s" % time.time()

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGWINCH, update)

while delays:
    signal.pause()
</code>

