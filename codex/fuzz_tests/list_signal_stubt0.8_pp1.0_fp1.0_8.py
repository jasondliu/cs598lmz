import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print(time.time())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.pause()
</code>
The idea is that the signal handler gets called by the kernel after a timer expires. The signal handler schedules the next timer expiration and then prints the current time. Since the kernel calls the signal handler, the process is blocked and can't do other work until the signal handler returns.

