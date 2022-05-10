import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, .5, .2)
import time
time.sleep(5)

signal.setitimer(signal.ITIMER_REAL, .5, .2)
time.sleep(5)
print('Done')

# Test signal.getitimer()
signal.setitimer(signal.ITIMER_REAL, .5, .2)
print('Starting')
time.sleep(1)
print('Continuing')
time.sleep(1)
print('Exiting')

import signal
signal.setitimer(signal.ITIMER_REAL, .5, .2)
print('Starting')
time.sleep(1)
print('Continuing')
time.sleep(1)
print('Exiting')

# Test signal.signal()
def handler(signum, frame):
    print(signum, frame)
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGALRM, handler)

