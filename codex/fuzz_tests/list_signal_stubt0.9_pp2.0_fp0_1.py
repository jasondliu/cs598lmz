import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print "Time's up!"
        os._exit(0)

signal.signal(signal.SIGALRM, handler)
handler()

try:
    while True:
        x = 1 + 1
except Exception as e:
    print e
