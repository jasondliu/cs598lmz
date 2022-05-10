import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        print("It is over")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

print("Start delay of %.8f seconds" % (delays[-1],))

while delays:
    pass
```
</details>

<details>
  <summary>Второй алгоритм</summary>
<br>

```python
import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

while delays:
    delays.sort()
    delay = delays.pop()
    print("Start delay of %.8f seconds" % (delay,))
    signal.alarm(delay)
    signal.pause()

print("It is over")
```
</details>

<
