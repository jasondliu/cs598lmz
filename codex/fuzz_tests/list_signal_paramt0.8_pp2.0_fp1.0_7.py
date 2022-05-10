import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

@coroutine
def compute():
    while True:
        signal.pause()
        print('compute')

@coroutine
def display():
    while True:
        signal.pause()
        print('display')

c = compute()
d = display()

for i in range(100):
    signal.pause()
    c.send('compute')
    d.send('display')
