import signal
# Test signal.setitimer()

import signal

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Restore the old signal handler for SIGALRM
signal.setitimer(signal.ITIMER_REAL, 0)

# Do something with fd

os.close(fd)
 

# The following code shows how to use the alarm() function to implement a
# timeout for a blocking operation.

import signal

class TimeoutError(Exception):
    pass

def timeout(seconds, error_message='Timeout'):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError
