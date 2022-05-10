import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

def do_something(n):
    print("Something doing. (%d)" % n)

i = 0
while delays:
    if random.random() < 0.5:
        do_something(i)
        i += 1
    else:
        time.sleep(random.random())

print("Done!")
