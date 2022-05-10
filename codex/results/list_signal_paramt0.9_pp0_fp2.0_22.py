import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def get_delay():
    t0 = time.time()
    while True:
        t1 = time.time()
        if t1 != t0:
            return t1 - t0

t1 = 1e10
for i in range(N):
    t0 = time.time()
    signal.setitimer(signal.ITIMER_REAL, delays[i])
    while not delays:
        pass
    t1 = min(t1, time.time() - t0)

t2 = 1e10
for i in range(N):
    delta = get_delay()
    t2 = min(t2, delta)

numerator = sum(delays) - N * t1 - N * t2
denominator = N * (1e-6 - t1 - t2)
print "reschedule overhead: %g\n  separate: %g\n" % (numerator / denominator, t2)

delays = sorted([int(d * 1
