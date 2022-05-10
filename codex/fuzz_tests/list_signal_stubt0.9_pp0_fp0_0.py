import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    print 'signum:', signum
    print 'time:', time.time()

signal.signal(signal.SIGALRM, handler)
handler()  # fire an event to start things
while True:  # loop while events are pending
    signal.pause()
