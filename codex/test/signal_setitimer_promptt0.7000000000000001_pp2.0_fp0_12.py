import signal
# Test signal.setitimer
# NOTE:
#   This does not properly test the alarm() function. For example, if this
#   test is run on a system that does not support the setitimer() function,
#   but does support the alarm() function, then this test will fail.

import signal
import os

