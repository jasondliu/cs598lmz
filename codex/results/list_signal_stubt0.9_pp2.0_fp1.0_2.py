import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print "pop", len(delays)

def gettimeout(timeout, granularity):
    return int(math.ceil(timeout / granularity)) * granularity

def set_timer(signum=None, frame=None):
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0)

signal.signal(signal.SIGALRM, set_timer)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)

while True:
    sleep(10)
