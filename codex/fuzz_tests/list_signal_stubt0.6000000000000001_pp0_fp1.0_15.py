import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
print('Timer started')

while delays:
    s = raw_input('Input anything: ')
    print('Input: %s' % s)
    time.sleep(1)
</code>
You can run this like this:
<code>$ python test.py 
Timer started
Input anything: a
Input: a
Input anything: b
Input: b
Input anything: c
Input: c
Input anything: d
Input: d
Input anything: e
Input: e
Input anything: 
</code>
I am not sure what you are trying to do, but I hope this code helps you understand how to use <code>signal</code> and <code>setitimer</code> better.

