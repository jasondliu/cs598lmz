import signal
# Test signal.setitimer()
#

import time
import signal

def sig_usr1(signum, frame):
    print("SIGUSR1 received")

signal.signal(signal.SIGUSR1, sig_usr1)
signal.setitimer(signal.ITIMER_REAL, 0.5)
print("Waiting for SIGUSR1")
signal.pause()

print("Done")
