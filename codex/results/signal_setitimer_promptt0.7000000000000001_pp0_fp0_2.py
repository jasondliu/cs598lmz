import signal
# Test signal.setitimer()
# The following routine schedules a timer to fire in a few
# seconds, sets a handler for SIGALRM, sets a timer for
# SIGALRM, and sleeps.  When the sleep completes, the handler
# for SIGALRM is called.
import time
def handler(signum, frame):
    print 'Signal handler called with signal', signum
    return
# Register the signal function handler
signal.signal(signal.SIGALRM, handler)
# Define a 5-second timer
seconds = 5
# Start the timer
signal.setitimer(signal.ITIMER_REAL, seconds)
print 'Sleeping...'
time.sleep(seconds + 5)
print 'Exiting...'
