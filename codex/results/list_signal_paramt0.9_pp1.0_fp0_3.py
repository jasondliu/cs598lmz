import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

def sleep_(); return lambda: None
old_signal = signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

for i in range(N):
    sleep_()
print delayed.f.__name__
</code>
The single call to sleep costs about 0.1s for me.

