import signal
# Test signal.setitimer()
#
# This test is specific to NetBSD, because it uses the setitimer(2) system call.
#
# This test does not run on other platforms, because signal.setitimer() raises
# an exception.
#
# XXX: The test is commented out, because it fails on NetBSD.
#      The test is kept in the source tree for further investigation.

if sys.platform != 'netbsd':
    raise unittest.SkipTest('test specific to NetBSD')

import errno
import os
import time
import _testcapi

from test import support
from test.support import get_attribute

# The following constants are defined in <sys/time.h>
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1
ITIMER_PROF = 2

# The following constants are defined in <signal.h>
SIGALRM = 14
SIGVTALRM = 26
SIGPROF = 27

# The following constants are defined in <errno.h>
EINVAL = 22

# The following constants are defined
