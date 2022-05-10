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

while delays:
    time.sleep(1)
```

The `time.sleep()` call blocks the current thread until the next signal
arrives.

The `signal.setitimer()` call sets the signal timer to the next time in the
list.

The `signal.signal()` call sets the signal handler to the handler function.

The handler function pops the next time from the list, and sets the signal
timer to this time.

The handler function also checks if the list is empty, and if so, it sets the
signal timer to 0 (i.e. disable the timer).

The `signal.ITIMER_REAL` is used to specify the type of timer.

The `signal.SIGALRM` is the signal to trigger when the timer expires.


