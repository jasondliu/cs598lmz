import signal
# Test signal.setitimer
os.kill(os.getpid(), signal.SIGALRM)
signal.setitimer(signal.ITIMER_REAL, 1)
time.sleep(2)
signal.setitimer(signal.ITIMER_REAL, 0)

import os, sys
