import signal
# Test signal.setitimer() function
# Author: Bob Halley

import signal
import time

def timer_handler(signum, frame):
    print('Signal handler called with signal', signum)

print('Registering alarm signal handler')
signal.signal(signal.SIGALRM, timer_handler)

seconds = 10
print('Setting timer for', seconds, 'seconds')
signal.setitimer(signal.ITIMER_REAL, seconds, 0)

print('Sleeping...')
time.sleep(20)

print('Done.')
