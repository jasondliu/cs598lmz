import signal
# Test signal.setitimer()
#
# $Id: setitimer.py,v 1.1 2007/07/24 07:23:27 gaufille Exp $

import os
import sys
import time
import signal

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Install the signal handler and set a itimer
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Set the itimer to zero, i.e. disable it
signal.setitimer(signal.ITIMER_REAL, 0)

# This open() works now
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Disable the alarm signal
signal.signal(signal.SIGALRM, signal.SIG_IGN
