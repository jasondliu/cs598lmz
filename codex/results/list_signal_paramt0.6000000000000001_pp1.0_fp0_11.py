import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)
handler()

def timer(delay):
    signal.setitimer(signal.ITIMER_REAL, delay)
    signal.pause()

def task():
    for i in range(10):
        print(i, '\n')
        time.sleep(1)

timer(0.5)

for i in range(N):
    task()
</code>
The issue is that the timer is not accurate. If I run the script and measure the time it takes to execute, I get something like this:
<code>$ time python timer.py
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6

