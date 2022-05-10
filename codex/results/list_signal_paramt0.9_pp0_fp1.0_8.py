import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
handler()
signal.pause()

import time

def foo():
    start = time.clock()
    time.sleep(1)
    end = time.clock()
    if 0.987 &lt;= start-end &lt;= 1.015:
        print('Good timing!')
    else:
        print('Bad timing!')

foo()
</code>
Related:

https://www.airs.com/blog/archives/54
Can my Python script send notifications every second?


