import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)

start = time.time()
while delays:
    time.sleep(1)
end = time.time()
print "delays: %.2f ms" % (end - start)

start = time.time()
for delay in delays:
    time.sleep(delay)
end = time.time()
print "time.sleep: %.2f ms" % (end - start)
