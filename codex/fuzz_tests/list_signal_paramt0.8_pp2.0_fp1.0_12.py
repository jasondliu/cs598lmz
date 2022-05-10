import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while delays:
    signal.pause()

signal.setitimer(signal.ITIMER_REAL, 0)
</code>
(It would be better to synchronize the events with the system clock, but this scheme is both cross-platform and accurate enough: the second timer will be triggered with a delay less than one second.)

