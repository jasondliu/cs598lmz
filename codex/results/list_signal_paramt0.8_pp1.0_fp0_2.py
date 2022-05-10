import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, max(delays), 0)
        delays.pop(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1e-6, 0)
signal.pause()
</code>
This seems to be close to what you want, but the timing is off, by several orders of magnitude. (The delays given in the list are accurate, but the delays between the signals are much longer, by about a factor of 1000.)

