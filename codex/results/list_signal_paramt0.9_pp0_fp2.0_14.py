import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print("{} events __main__".format(len(events)))
        print("{} calls to f1".format(len(events_f2)))
        print("{} calls to f2".format(len(events_f1)))
        sys.exit(0)

handler()
signal.signal(signal.SIGALRM, handler)

@trace
def f1(a, b):
    tmp = a + b
    return tmp

@trace
def f2(n):
    for i in range(100000):
        f1(i, i)

for i in range(100000):
    f2(i)
