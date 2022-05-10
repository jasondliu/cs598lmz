import signal
# Test signal.setitimer()
#
# This test is not run by default.  It requires the program to be run
# as root, and it uses the alarm() system call, which is not available
# on all systems.
#
# The test will run for about 10 seconds, and then print a message
# indicating whether it passed.

import os
import sys
import time

from test.support import verbose, TestSkipped

