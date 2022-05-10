import signal
# Test signal.setitimer()
#
# This test is not very good, since it depends on the system clock.
# It will fail if the system clock is changed during the test.

import signal, time

