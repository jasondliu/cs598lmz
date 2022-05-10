import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('Done')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
while delays:
    signal.pause()
</code>
This is an example of how to do it with <code>multiprocessing</code> instead.
<code>import multiprocessing
import random

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def do_work(delay):
    # Do the work
    pass

def handler(delay):
    do_work(delay)
    if delays:
        multiprocessing.Process(target=handler, args=(delays.pop(),)).start()
    else:
        print('Done')

multiprocessing.Process(target=handler, args=(delays.pop(),)).start()
</code>

