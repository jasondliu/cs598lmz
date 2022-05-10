import signal
# Test signal.setitimer() and signal.getitimer()
try:
    signal.setitimer
    signal.getitimer
except AttributeError:
    raise unittest.SkipTest("test requires setitimer/getitimer")

import select
import time
import errno

from test.support import reap_threads

if hasattr(signal, "set_wakeup_fd"):
    set_wakeup_fd = signal.set_wakeup_fd
else:
    set_wakeup_fd = None

have_real_timer = hasattr(signal, 'setitimer')
have_monotonic_clock = getattr(time, 'monotonic', None) is not None

# On Mac OS X setitimer doesn't work with threads
require_threads = sysconfig.get_config_var('THREADHEADERS') == '"pthread.h"'

# Some tests of signal.setitimer() and signal.getitimer()
# depend on the timer resolution, which varies across platforms.
# To avoid those tests taking too long, we use the following timer
#
