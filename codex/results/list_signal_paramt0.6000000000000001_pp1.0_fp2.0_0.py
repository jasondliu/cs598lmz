import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print("Done")
        sys.exit(0)


signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    signal.pause()
</code>
This code works just fine, however if I try to use <code>signal.setitimer</code> with <code>signal.ITIMER_REAL</code> or <code>signal.ITIMER_VIRTUAL</code> then the code gets stuck in the <code>while delays:</code> loop. I've tried using <code>signal.siginterrupt(signal.SIGALRM, False)</code>, but it doesn't help.
I'm using Python 3.3.
What am I missing?


A:

I've found the solution.
It seems that Python 3.3 does not interrupt <code>signal.pause()</code> by default.
If I use <code>signal.siginterrupt(signal.SIGALRM, True
