import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(
            signal.ITIMER_REAL, delays.pop(0)
        )
    else:
        sys.stdout.write(".")
        sys.stdout.flush()
    return

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

i = 0

while True:
    try:
        i += 1
    except KeyboardInterrupt:
        break
