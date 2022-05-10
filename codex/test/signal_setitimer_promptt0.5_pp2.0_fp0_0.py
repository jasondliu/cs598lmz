import signal
# Test signal.setitimer() and signal.getitimer()

import signal
from test import support

def handler(signum, frame):
    print('handler called')

signal.signal(signal.SIGALRM, handler)

# setitimer() should return (0, 0)
print(signal.setitimer(signal.ITIMER_REAL, 0.5, 0))

# getitimer() should return (0.5, 0)
print(signal.getitimer(signal.ITIMER_REAL))

# setitimer() should return (0.5, 0)
print(signal.setitimer(signal.ITIMER_REAL, 0, 0))

# getitimer() should return (0, 0)
print(signal.getitimer(signal.ITIMER_REAL))

# setitimer() should return (0, 0)
print(signal.setitimer(signal.ITIMER_REAL, 0.5, 0))

# getitimer() should return (0.5,
