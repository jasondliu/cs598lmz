import signal
# Test signal.setitimer()
#
# This test is not very comprehensive, but it does at least
# exercise the code.
#
# XXX This test currently fails on FreeBSD, because the
# signal handler is not called.  This is a bug in FreeBSD.

import sys
import time
import unittest
from test.support import run_unittest, requires_resource

# Test that signal.setitimer() works.
#
# The test is a bit tricky, because we want to test that the
# signal handler is called, and that it is called with the
# correct argument.  We can't just set a flag in the signal
# handler, because the signal handler could interrupt the test
# code in the middle of testing the flag.  So instead, we set
# a flag in the signal handler, and then we use signal.pause()
# to wait for the signal handler to be called.  signal.pause()
# will return when a signal is received.  If the signal handler
# is called with the correct argument, then the signal handler
# will call signal.alarm(0), which will cause signal.pause() to
# return immediately.
