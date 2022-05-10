import signal
# Test signal.setitimer
#
# This test is not very useful.  It just makes sure that setitimer()
# doesn't crash the interpreter.

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.2)
