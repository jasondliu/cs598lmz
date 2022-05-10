import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    print "called", signum, frame

for sig in [signal.SIGALRM, signal.SIGVTALRM, signal.SIGPROF]:
    signal.signal(sig, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop())

for i in range(N):
    signal.pause() # wait for signal
</code>


A:

The signal handler may be run at any time (including when your code is not in Python).
In the case of SIGPROF and SIGALRM, the signal is delivered when the timer expires, so it will be at most a few microseconds late. 
However, the handler will only be invoked when your code is in native code, so it may be arbitrarily off as far as your Python code is concerned. Your Python code will be interrupted after the signal handler returns, and won't return until your code finishes executing other Python code, so it could be a significant fraction of a second (or more), depending on your Python code.
As far as I know,
