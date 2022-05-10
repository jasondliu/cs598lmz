import signal
# Test signal.setitimer
#
# This test case ensures that signal.setitimer() works as expected.

import signal, time

def handler(sig, frame):
    raise RuntimeError("Timeout")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.5)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.5)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.5)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.5)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.5)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.5)
signal.setitimer(
