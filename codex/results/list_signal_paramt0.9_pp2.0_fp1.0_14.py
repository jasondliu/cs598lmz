import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer()
        time.sleep(delays.pop(0))


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, handler)
    handler()
    while delays:
        time.sleep(1)
</code>
I thought the code would sleep for N intervals, but it terminates early.
This happens on Systems with Python2.7 and Python3.4, but not with Python-2.6
Any ideas?


A:

In your code, you are removing a random element from delays, so the length of delays will gradually decrease, so your number of iterations will also decrease. To avoid this, you can use <code>delays[i]</code> instead of <code>delays.pop(0)</code>
The code below works for me:
<code>import signal
import time
import random
N = 10000
random.seed(1)
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
       
