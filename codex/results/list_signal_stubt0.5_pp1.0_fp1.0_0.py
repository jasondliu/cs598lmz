import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('Done')
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
```

## 参考

- [How to set a timer in Python?](https://stackoverflow.com/questions/3393612/how-to-set-a-timer-in-python)
- [Python Signal Processing](https://www.tutorialspoint.com/python/python_signal_processing.htm)
