import signal
# Test signal.setitimer()
#
# This test is Linux-only; it relies on the ITIMER_PROF timer,
# which is not supported on any other platform.

import os, signal, time

if signal.setitimer(signal.ITIMER_PROF, 0.5, 0.5) == 0:
    raise ValueError("setitimer() requires an interval")

