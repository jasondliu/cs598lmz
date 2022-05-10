import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

for i in range(N):
    print(i)
    time.sleep(1e-6)
</code>
If you have a lot of different timers to manage, you might consider using the <code>select</code> module, which allows you to wait on multiple file descriptors.  In this case, you can use the <code>signalfd</code> function to create a file descriptor which you can wait on for the signal.

