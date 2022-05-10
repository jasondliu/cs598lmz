import signal
# Test signal.setitimer
#
# This test is not very good, because it relies on the timer being
# accurate to the millisecond, and it doesn't test the case where the
# signal handler is interrupted by another signal.
#
# Written by Fred L. Drake, Jr. <fdrake@acm.org>
# and placed in the public domain.

import os
import signal
import sys
import time

# The test is run in a subprocess, so that the signal handler can be
# installed without affecting the main process.

