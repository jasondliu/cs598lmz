import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0.0)

def all_done():
    print("Done.")
    signal.signal(signal.SIGALRM, signal.SIG_DFL)

signal.signal(signal.SIGALRM, handler)
signal.alarm(1)
signal.siginterrupt(signal.SIGALRM, False)

print("Wait for it...")
try:
    signal.pause()
except KeyboardInterrupt:
    all_done()
</code>

