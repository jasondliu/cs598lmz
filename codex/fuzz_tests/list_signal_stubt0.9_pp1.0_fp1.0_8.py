import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

for j in range(100):
    for i in range(10):
        print(i, end=" ")
        sys.stdout.flush()
        time.sleep(1)
    print()
</code>
The sequence of delays is built beforehand by drawing from a uniform distribution and then reversed so that pop() won't need to shuffle remaining values. Also, the number of iterations is set to 100 (default is 10) since you don't get the output right away and 100 iterations are roughly 1 minute. The timer is armed by a signal handler after the delay is popped off the stack, thus resetting itself every time.
The output looks like this:
<code>$ python test.py
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1
