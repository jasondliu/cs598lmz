import signal
# Test signal.setitimer()
def handler(signum, frame):
    print("Received:", signum)

# Register the signal function handler
signal.signal(signal.SIGALRM, handler)

# Define a timeout for your function
seconds = 5

# setitimer() to generate a signal after 5 seconds
signal.setitimer(signal.ITIMER_REAL, seconds)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(seconds)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Reset the alarm
signal.alarm(0)

# Do something with fd
import os
import signal

def handler(signum, frame):
    print("Forever is over!")
    raise Exception("end of time")

# Register the signal function handler
signal.signal(signal.SIGALRM, handler)

# Define a timeout for your function
