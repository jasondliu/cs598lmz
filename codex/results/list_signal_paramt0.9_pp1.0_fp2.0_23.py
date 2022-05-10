import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

# set up a signal handler
signal.signal(signal.SIGALRM, handler)

# program handler to fire first time
delay = delays.pop()
signal.setitimer(signal.ITIMER_REAL, delay)

# wait for timer signals
while delays:
    import time
    time.sleep(5)
</code>

