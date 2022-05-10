import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        print('Done')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays: time.sleep(.5)
```

```
$ python timer.py
Done
```

Note that the signal handler is not guaranteed to be called at the exact moment
the timer expires, but the system guarantees that the delay between the expiry
of the timer and the invocation of the signal handler will not be more than the
system clock granularity.

## 4.3.3 Timing Events in Other Threads

```
$ python timer_multithread.py
Thread 1: 0.000997
Thread 2: 0.000999
Thread 3: 0.000999
Thread 4: 0.000999
Thread 5: 0.000999
Thread 6: 0.000999
Thread 7: 0.001000
Thread 8: 0.001000
Thread 9: 0.
