import signal
# Test signal.setitimer() under Linux (and possibly other python2.2 builtin
# implementation).
# Under this implementation, the following test make a lot of sense.

# In python3.1, the setitimer() implementation has been replaced by a call
# to the libc's setitimer() in the signalmodule.c file.
# In the python2.2 implementation from the signalmodule.c file:
#  - the time is expressed in milliseconds,
#  - the timer sets its own thread as SIGALRM handler
#  - it uses the SIGALRM to switch between threads.
# As a consequence, the timer is not shared among the threads.
# So this test is no more relevant for python3.1+.

from test_support import TestSkipped
