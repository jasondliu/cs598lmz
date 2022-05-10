import signal
# Test signal.setitimer()
#
# Note that this test can't be run in a subprocess, as the
# signal module checks for the presence of the ITIMER_REAL
# constant (which is not imported into the subprocess's namespace).
