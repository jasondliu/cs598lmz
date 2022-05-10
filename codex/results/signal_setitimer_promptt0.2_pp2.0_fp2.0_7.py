import signal
# Test signal.setitimer()
#
# This test is a bit different from the others.  It is not run by
# the test runner, but instead is run by the test harness.  The
# harness runs the test in a subprocess, and then checks the output
# of the subprocess.  The output should look like this:
#
#     $ ./python -u ./Lib/test/test_signal.py
#     signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
#     signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
#     signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
#     signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
#     signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
#     signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
#
