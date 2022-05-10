import signal
# Test signal.setitimer() to see if it will work.
try:
    signal.signal(signal.SIGALRM, signal.SIG_DFL)
    signal.setitimer(signal.ITIMER_REAL, 0, 1)
except:
    HAVE_SETITIMER= False
else:
    HAVE_SETITIMER= True
    signal.setitimer(signal.ITIMER_REAL, 0, 0)

import sys
if sys.platform == 'win32':
    HAVE_SETITIMER= False

if HAVE_SETITIMER:
    class Task(object):
        """Task(callback, interval, repeat)

        This class is a wrapper around signal.setitimer that allows you to
        schedule a callback to be called at a specified time.  The callback
        is called repeatedly at the specified interval until a repeat count
        of 0 is specified.  The callback is called with one parameter, a
        float indicating the elapsed time since the last callback.
        """
        def __init__(self, callback, interval, repeat):
            self.callback= callback
