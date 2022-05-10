import signal
# Test signal.setitimer

import time

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Do some processing here
time.sleep(10)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)
os.close(fd)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Set an alarm
signal.setitimer(signal.ITIMER_REAL, 1)

# This read() may fail with EINTR
s =
