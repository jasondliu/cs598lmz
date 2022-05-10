import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>


A:

You can use a counter to track the number of iterations across threads.
<code>import threading
import time

total = 0

def f():
    global total
    while total &lt; 100:
        print(total)
        total += 1
        time.sleep(1)

for _ in range(5):
    threading.Thread(target=f).start()
</code>

