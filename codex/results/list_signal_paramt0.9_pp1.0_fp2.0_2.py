import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    print(len(delays))


signal.signal(signal.SIGALRM, handler)
signal.siginterrupt(signal.SIGALRM, True)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.pause()
</code>
Expected output:
<code>$ time python3 thread_delay.py &gt; /dev/null

real    0m8.170s

$ time python3 signal_delay.py &gt; /dev/null

real    0m6.884s
</code>

