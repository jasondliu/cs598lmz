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
    try:
        signal.pause()
    except KeyboardInterrupt:
        print('\nDone')
        break
</code>

<code>$ python3.4 timer.py
^C
Done

$ time python3.4 timer.py &gt;/dev/null 

real    0m0.323s
user    0m0.036s
sys     0m0.044s
</code>

