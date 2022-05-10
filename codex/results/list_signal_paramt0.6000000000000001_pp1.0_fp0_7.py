import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        print('Done')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1e-6)

while delays:
    # This sleep is necessary, otherwise the handler function
    # is called only once.
    time.sleep(1e-10)
