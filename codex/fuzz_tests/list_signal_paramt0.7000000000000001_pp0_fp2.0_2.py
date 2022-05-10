import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
        signal.alarm(delays.pop())

signal.signal(signal.SIGALRM, handler)
handler()

try:
    while delays:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
</code>
I tried to use the <code>threading</code> module but it seems that it can't be used in conjunction with the <code>signal</code> module.
I'm open to any suggestions on how to do this.

