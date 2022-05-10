import signal
# Test signal.setitimer() and signal.getitimer()

import time

def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGALRM, handler)

# Register handler for SIGALRM
# Set an alarm
signal.setitimer(signal.ITIMER_REAL, 2)

print('Sleeping')
time.sleep(4)
print('Exiting')
