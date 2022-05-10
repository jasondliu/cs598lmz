import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print 'bang'

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
try:
    while 1:
        pass
except KeyboardInterrupt:
    print '\nciao'
</code>


A:

Here the code to compute random uniform delays:
<code>import random
import signal

N = 10000000
min_delay = 0.5e-6
max_delay = 0.6e-6
delays = [
    (min_delay + (max_delay - min_delay) * random.random())
    for i in range(N)
]
</code>
Probably the code is not random uniform enough so I used the code from this answer to be sure that it is random uniform. Now I have added an error in the computation of <code>delta</code> so that the result is not random uniform. How to detect it?
Here I used to compute the mean of the delays:
<code>def mean(l):
    return sum
