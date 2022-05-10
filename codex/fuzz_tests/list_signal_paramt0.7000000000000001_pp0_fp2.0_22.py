import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit()

signal.signal(signal.SIGALRM, handler)

handler()

# In Python 2, we could just call signal.pause() to wait for the next 
# SIGALRM. In Python 3, that function has been removed.
#
# https://docs.python.org/3/library/signal.html#signal.pause

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
