import signal
# Test signal.setitimer()
# This test is for FreeBSD only, as setitimer() is not available on Linux.
# For other platforms, the test is skipped.

import signal, os, time, errno

