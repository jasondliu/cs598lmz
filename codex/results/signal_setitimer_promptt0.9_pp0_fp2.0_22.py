import signal
# Test signal.setitimer
#

import os, sys
from test.test_support import verify, TestFailed

def check(sig, v):
    if v != getitimer(sig):
        raise TestFailed("%s using setitimer and getitimer: %s != %s" % (
            sig, v, getitimer(sig)))

signums = ['SIGALRM', 'SIGVTALRM', 'SIGPROF']
signums = [getattr(signal, x) for x in signums]
def test_setitimer():
    for sig in signums:
        r = setitimer(sig, 1.5, 0)
        check(sig, (1.5, 0))

        # make sure we actually do get the alarm
        setitimer(sig, 0.1, 0)
        alarm_triggered = [False]
        def alarm_handler(sig, frm):
            alarm_triggered[0] = True
        signal.signal(sig, alarm_handler)
        # wait long enough that we
