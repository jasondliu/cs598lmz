import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
```

And the results:

```
$ python3 signal_timer.py

real	0m1.073s
user	0m0.093s
sys	0m0.009s
```

So, using a timer to trigger an event is about 10 times slower than using a
regular loop.

To be fair, I should point out that the loop is performing a very simple
calculation, while the timer is actually calling a function, which is more
expensive.

I then tried to compare the two approaches by making the loop do something more
interesting:

```python
import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None
