import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)
        s = signal.SIGALRM # pylint:disable=no-member
        signal.signal(s, handler)
    else:
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

s = signal.SIGALRM # pylint:disable=no-member
signal.signal(s, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)

while delays:
    signal.pause()
</code>
Note that on some Unix system (OS X, at least), you'll find that your timeout handler gets called twice as often as expected. This is expected behavior on OS X, where CPU time and so forth is charged against threads, not processes. In this case, every call to <code>pause</code> ends up costing you twice as much time.

