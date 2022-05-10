import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0) # stop timer

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

# do work

signal.pause()
</code>
The distribution of time between alarms is uniform, and each alarm is processed immediately. I've successfully used something like this to drive a media player to play a movie frame-accurately.

