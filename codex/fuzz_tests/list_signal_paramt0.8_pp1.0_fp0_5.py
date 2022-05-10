import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
        print len(delays)
    else:
        print("no more delays")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
</code>
but I get an OverflowError:
<code>    signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
OverflowError: signed integer is greater than maximum
</code>
when I change it to <code>ITIMER_VIRTUAL</code> it works, but due to the limits of the timer, I can't get more than about <code>1000</code> timers (for my timer granularity).
Updates:

Removed <code>* 1e6</code> from <code>N</code>, which I mistakenly thought was necessary to make the correct units due to how I generated the delays.
Tried <code>signal.setitimer(signal.ITIMER_PROF, delays.
