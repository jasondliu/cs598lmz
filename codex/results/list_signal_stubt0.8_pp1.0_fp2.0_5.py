import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

def long_op():
    for i in range(int(1e5)):
        pass

while delays:
    long_op()
</code>
I am wondering if the <code>long_op</code> procedure gets interrupted by the <code>SIGALRM</code> signal or if it doesn't get interrupted and the signals are being handled in the order they are received. That is, does the above code output a random sequence of numbers or will it always output numbers in increasing order?
Some important information about my case is that the thing I am doing in the <code>long_op</code> procedure can be interrupted safely, so it isn't a problem if the procedure is interrupted at some point.
I am using Python 3.8.2 on Ubuntu 20.04, but I would like to know whether the order in which primitive ops are interrupted is guaranteed to be consistent across platforms.


A:

Per the python docs:
<blockquote>

