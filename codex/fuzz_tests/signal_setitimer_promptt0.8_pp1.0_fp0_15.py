import signal
# Test signal.setitimer() by making it send a SIGALRM once every half
# second.
#
# Based on test_signal.py by Eric Tiedemann.

import sys

#
# find out what the default signal handler is
#
old = signal.getsignal(signal.SIGALRM)

#
# define a new signal handler
#
#def handler(signum, frame):
#    global hitcount
#    hitcount = hitcount+1
#    raise IOError, 'alarm'


#
# set a new signal handler
#
#signal.signal(signal.SIGALRM, handler)

#
# setitimer() will cause our signal handler to be invoked once
# every half second.
#
#signal.setitimer(signal.ITIMER_REAL, 0.5, 1.0)

#
# In order to measure the time delay, we reset the alarm alarm.
#
#hitcount = 0
#start = time.time()
#signal.alarm(1)
#
# Now we wait long
