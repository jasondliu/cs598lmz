import signal
# Test signal.setitimer and signal.getitimer.
#
import time
#
# this should be in <sys/resource.h>
#
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1
ITIMER_PROF = 2

def alarm_handler(signum, frame):
    pass

## signal.setitimer
## signal.getitimer
#
# Set and read the real timer to check its value.
#
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(ITIMER_REAL, 1, 0)
r = signal.getitimer(ITIMER_REAL)
time.sleep(2.0)
r2 = signal.getitimer(ITIMER_REAL)
