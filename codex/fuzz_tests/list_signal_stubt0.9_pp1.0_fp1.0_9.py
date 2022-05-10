import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
sys.setcheckinterval(1)

L = []
i = 0
j = 0

while delays:
    i += 1
    L.append(i % 1)
    for j in range(len(L)):
        if L[j] == 1:
            L.remove(L[j])
    j += 1
