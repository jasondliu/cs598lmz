import signal
# Test signal.setitimer()
#
# This test is for the case when a signal handler is called
# while the signal is blocked.
#
# The test sets up a timer to fire a signal after a few seconds.
# The handler for the signal blocks the signal, sets up a new
# timer to fire after a few more seconds, and then unblocks
# the signal.
#
# The test is successful if the second timer fires.
#
# This test is a bit tricky because the signal handler needs to
# be able to set up the second timer.  The signal handler
# can't call setitimer() directly because it's not async-signal
# safe.  Instead, the signal handler sets a flag, and the main
# program checks the flag every so often.  When the flag is set,
# the main program calls setitimer() to set up the second timer.
#
# This test is not run on Windows because Windows doesn't support
# setitimer().

if os.name == 'nt':
    raise unittest.SkipTest('test not appropriate for Windows')

import time
