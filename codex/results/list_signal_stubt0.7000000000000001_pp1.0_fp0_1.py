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
    signal.pause()

print('done')
```

### 3.2.2.2. `alarm`

`alarm` 函数设置一个秒级的定时器，只能设置一次，设置多次后会覆盖之前的设置。

`alarm` 是时间到达后会发送 `SIGALRM` 信号。

`alarm` 可以用来设置一个定时器，
