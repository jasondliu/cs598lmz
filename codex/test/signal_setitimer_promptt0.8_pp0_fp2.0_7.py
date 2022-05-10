import signal
# Test signal.setitimer() on multiple threads
#
# This test should run in a reasonable time (less than a second)
#
# Note that this test is *not* enabled by default, as it only applies to
# builds which support thread cancellation (enabled by configure with
# --enable-thread-cancellation)

# Skip test if no thread support
import support
support.requires('thread')
support.check_impl_detail(pypy=False)

import _testcapi
import test.support
import time, os

# on older versions of linux, this is needed to enable a special
# wrapper for signals that lets glibc's malloc work in threaded
# programs.
if hasattr(_testcapi, 'SA_RESTART'):
    import signal
    signal.SA_RESTART

# The test is only relevant on platforms with support for
# thread cancellation.
if not test.support.threading_setup():
    raise test.support.TestSkipped("thread cancellation")

