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
</code>
This code will generate <code>N</code> random delays between 1 microsecond and 3 microseconds, and set up a timer to fire <code>N</code> times, each one waiting the corresponding delay.
This program will block most of the time in the <code>signal.pause()</code> call, which means it will not be using any CPU time (and thus not be interrupting anything else).

