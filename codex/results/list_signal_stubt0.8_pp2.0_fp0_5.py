import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("Done")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop())

while True:
    time.sleep(1)
</code>

The code above was edited to reduce the delay to 10ms max, with a few microseconds of variation. The resulting histogram is as follows:


