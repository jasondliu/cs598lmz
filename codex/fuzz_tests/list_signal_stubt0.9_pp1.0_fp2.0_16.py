import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
         print("It is enough!")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    print("Do some job")
</code>


A:

With Kqueue notification, you can define a signal threshold, the maximum number of events (signals in this case) that you want to process at once. It is useful to avoid signal loss if the signal queue is full. Set it on a per file  basis:
<code>kevent.flags = EV_SET | EV_CLEAR;
kevent.filter = EVFILT_SIGNAL;
kevent.ident = SIGRTMIN + 3;
kevent.data = 42; // or 0 to indicate no threshold
kevent.udata = (void *) &amp;counter;

kevent(kq, &amp;kevent, 1, NULL, 0, NULL)
</code>
More details there

