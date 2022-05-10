import signal
# Test signal.setitimer vs. signal.settimer.  These two interfaces are similar,
# but not quite the same.
import os
import sys
import time
from test.support import import_module

supports_setitimer = hasattr(signal, 'setitimer')
print_ = getattr(sys.stdout, 'write', print)
print_('supports_setitimer =', supports_setitimer)

# Test whether setitimer(ITIMER_VIRTUAL) is too broken to use
# XXX SIGVTALRM is not used by the Python interpreter

if supports_setitimer:
    from _testcapi import getitimer_if_available
    import _testcapi
    old_interval = getitimer_if_available(signal.ITIMER_VIRTUAL)
    _testcapi.set_alarm_interval(0.01)

    for i in range(5):
        signal.signal(signal.SIGVTALRM, signal.SIG_IGN)
        time.sleep(0.02)
        new_interval =
