import signal
# Test signal.setitimer()
# The following routine schedules a timer to fire in a few
# seconds, sets a handler for SIGALRM, sets a timer for
# SIGALRM, and sleeps.  When the sleep completes, the handler
# for SIGALRM is called.
import time
