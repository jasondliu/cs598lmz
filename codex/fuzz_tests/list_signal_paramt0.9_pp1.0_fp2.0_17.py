import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.signal(signal.SIGALRM, handler)
handler()

def could_be_suspended():
    t = time.time()
    while time.time() - t < 0.01e-3:
        x = 1 + 1
    x = 1 + 1

while delays:
    could_be_suspended()
