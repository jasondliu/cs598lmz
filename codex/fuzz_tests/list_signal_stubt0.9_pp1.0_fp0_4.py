import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit(0)

counter = [0]          # Count the signals using a mutable list

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while True:
    delay = random.choice([1e-5, 1e-6])
    counter[0] += 1
    time.sleep(delay)
