import signal
# Test signal.setitimer()
#
# Note that if you enable SIGALRM, then you have to enable
# it in the thread where you are waiting for input.
# Otherwise it is used by the background thread that
# interprets the alarm signal.
#
# If you enable SIGALRM and then call setitimer(), then
# you will never get the signal.
#
# If you call setitimer() and then enable SIGALRM, then
# it will work.
#
# See also:
#
#     http://stackoverflow.com/questions/492519/timeout-on-a-python-function-call
#
#     https://docs.python.org/3/library/signal.html#signal.setitimer
#
#     https://docs.python.org/2/library/signal.html#signal.signal

# Note: if you use signal.SIGALRM, then you should disable it
# before starting the thread that waits for the input, otherwise
# that thread will never get the signal.

import signal
import time

class InputTimeout(Exception): pass

