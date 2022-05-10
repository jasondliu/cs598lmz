import signal
# Test signal.setitimer()
import sys
import time

print("SIGALRM = ", signal.SIGALRM)

def handler(signum, frame):
    print('Signal handler called with signum', signum)
    raise OSError("Boom!")

# Call handler() when the signal arrives
signal.signal(signal.SIGALRM, handler)

# This is supposed to print 'Boom!', but doesn't work
# on all platforms.

for i in range(5):
    print("Wait", i + 1, "seconds")
    signal.setitimer(signal.ITIMER_REAL, 1)
    time.sleep(1)

# If a signal handler raises an exception, the program will
# be terminated with a traceback.

# On Mac OS X, the program will be terminated without a
# traceback.

# On Windows, setitimer() is not available, and instead
# signal.alarm() is used.

# On Windows, this program will be terminated without a
