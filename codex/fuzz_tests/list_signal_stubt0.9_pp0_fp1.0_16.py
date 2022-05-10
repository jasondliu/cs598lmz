import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
handler()
while True:
    signal.pause()
</code>
This doesn't sleep inbetween the 100 timers set, but it is quite usable if you call your blocking operation after the signal is received.

