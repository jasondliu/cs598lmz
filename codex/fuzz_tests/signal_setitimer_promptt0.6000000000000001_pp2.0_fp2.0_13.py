import signal
# Test signal.setitimer

import time

def alarm_handler(signum, frame):
    print('Got SIGALRM')

signal.signal(signal.SIGALRM, alarm_handler)

# The first timer will fire in 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# The second timer will fire in 0.5 seconds
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.25)

time.sleep(3)

# Disable the timer
signal.setitimer(signal.ITIMER_REAL, 0)

# The timer is disabled, so this will never be reached
time.sleep(1)
