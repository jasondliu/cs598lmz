import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

start = time.time()

while 1:
    pass
</code>
This code will issue a SIGALRM every 100 to 300 microseconds, which should be accurate to a microsecond or so.  But...the code will lock up after about 9300 iterations.
I'm running Python 3.2.2 on 64bit linux (Fedora 17), and 64 bit Python 2.7.3 behaves the same way.
If I remove the 'delays.pop()' operation, then the code will run correctly.  Or, if I change the list comprehension to return a constant instead of 'random.random()', then it runs correctly.  If I increase N to 100000, then it still hangs after 9300 iterations.
Any ideas why this code is locking up?  Is it a bug?
Update: I filed a bug report with Python's bug tracker: http://bugs.python.org/issue15424


A:

This was a bug in Python 2.7
