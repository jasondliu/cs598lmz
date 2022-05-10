import signal
# Test signal.setitimer()
import sys
import os
import time

# this is the handler for the alarm
def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Timeout")

# register the handler
signal.signal(signal.SIGALRM, handler)

# set the alarm
signal.setitimer(signal.ITIMER_REAL, 0.1)

# this will run for 5 seconds
try:
    while True:
        print "Running"
        time.sleep(1)
except IOError:
    print "Timeout"
</code>
This works well, but the problem is that the alarm is not reset when the handler is called.
I could set the alarm again in the handler, but this means that the handler is called again after 0.1 seconds, which is not what I want. I want to set the alarm once, and have it reset every time the handler is called.
I could also try to reset the alarm in the main loop, but this would be a hack, as I want to be able to call the alarm in other functions as well
