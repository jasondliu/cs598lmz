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
    print('.', end='', flush=True)
    time.sleep(2)
</code>
The above is proof-of-concept for a simulation of a microcontroller application and was tested with Python 3.6 on OSX.

