import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop(0))
    else:
        signal.setitimer(signal.ITIMER_VIRTUAL, 0)

signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop(0))
```

Timers, you’ll recall, are process-wide and the resolution is much coarser
than a single instruction. For example, on my Linux system, the smallest
interval is 10 milliseconds. This will interfere with other things that
use timers, including Python’s own timer thread, so use this with care.

The other option for timers is to use a signal handler for SIGALRM and
`setitimer(ITIMER_REAL, ...)`, which is much more precise than ITIMER_VIRTUAL.
The resolution is the same as `time.sleep()`, but there’s the problem of
interference with other code that uses the timer.

You can also try polling the current time with `time.mon
