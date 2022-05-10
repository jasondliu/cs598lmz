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

print('Done')
</code>
When running on my Linux machine, I get
<code>$ time python3 test.py
Done

real    0m10.056s
user    0m0.000s
sys     0m0.004s
</code>
The <code>time</code> command indicates that the Python script took 10.056 seconds to run.

<blockquote>
<p>Is there a way to get more accurate information about the execution time without introducing too much overhead?</p>
</blockquote>
If you don't care about the CPU time then the <code>time</code> command is the best way to go. If you care about the CPU time then you are out of
