import signal
# Test signal.setitimer() and signal.getitimer()

import signal, os

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# This call sets an alarm to go off in 5 seconds
signal.setitimer(signal.ITIMER_REAL, 5)

# This read waits until a signal arrives
print 'Before pause'
signal.pause()
print 'After pause'
