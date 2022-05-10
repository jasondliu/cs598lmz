import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print('#', end='')

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)

print('Press Ctrl+C to stop')
while True:
    signal.pause()

# Press Ctrl+C to stop
# ################################
</code>

