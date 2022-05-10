import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print("Last remaining timer expired")
        assert not r.keys("*")
        sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

i = 1
while True:
    for j in range(100):
        r["foo:" + str(i)] = i
        i += 1
    print("%d keys set" % i)
