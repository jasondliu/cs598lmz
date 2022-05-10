import signal
# Test signal.setitimer()
#
# The test is to start a timer and then send a signal to the process.
# The signal handler should then check that the timer has expired.

import os
import sys
import time
import signal

# The time to wait for the timer to expire
TIMER_TIMEOUT = 1

# The time to wait for the signal to arrive
SIGNAL_TIMEOUT = 2

# The signal to send
SIGNAL_NUMBER = signal.SIGUSR1

# The time to wait for the timer to expire
TIMER_TIMEOUT = 1

# The time to wait for the signal to arrive
SIGNAL_TIMEOUT = 2

# The signal to send
SIGNAL_NUMBER = signal.SIGUSR1

# The time to wait for the timer to expire
TIMER_TIMEOUT = 1

# The time to wait for the signal to arrive
SIGNAL_TIMEOUT = 2

# The signal to send
SIGNAL_NUMBER = signal.SIGUSR1

# The time to wait for the timer to expire
TIMER_TIMEOUT = 1

