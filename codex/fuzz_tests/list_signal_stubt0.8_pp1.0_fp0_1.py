import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        raise RuntimeError()
    else:
        exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while True:
    print "hello"

while True:
    print ("hello")

def foo():
    for x in range(N):
        yield (x**2)

for x in foo():
    print x
