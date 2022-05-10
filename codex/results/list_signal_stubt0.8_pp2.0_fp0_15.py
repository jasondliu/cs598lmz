import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        signal.signal(signal.SIGALRM, handler)
    else:
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    time.sleep(delays[-1] * 1.1)
</code>
But if you have extra CPU time anyway, you might as well just run the loop 10 times faster and wait 10 times less between handlers invocations.

