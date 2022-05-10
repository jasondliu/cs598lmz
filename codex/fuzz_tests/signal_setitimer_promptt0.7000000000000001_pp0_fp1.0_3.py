import signal
# Test signal.setitimer()
#
# This test is not included in the main test suite because it requires
# root priviledges.
#
# If the test is run using 'sudo', then this program will attempt to
# raise a real-time signal every second. If the test is run as a
# non-privileged user, this program will only attempt to raise a
# virtual timer signal.
#
# The test program is supposed to exit when the test is complete. If
# it fails to do so, it will be killed after 5 minutes.
#
# A. S. Hodel <scotte@ieee.org>
#

from __future__ import print_function
from __future__ import division

from test_support import verbose, verify
import time, sys, os
from signal import *

if verbose:
    print(sys.version)
    print('pid', os.getpid())

# If test is run as root, we will attempt to generate a real-time
# signal every second.
#
# If test is run as a regular user, we will attempt to generate a
# virtual timer signal every second.
