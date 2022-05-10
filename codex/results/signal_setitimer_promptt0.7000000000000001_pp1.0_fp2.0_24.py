import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL)
#
# This test attempts to run a process for exactly 1 second.
#
# The test works by setting a SIGALRM to go off in 1 second.  When the
# SIGALRM goes off, the process exits.  If the process runs for longer
# than 1 second, the test fails.
#
# This test uses the ITIMER_VIRTUAL timer (a.k.a. the "process" timer)
# because that's the only timer that's guaranteed to run while the
# process is running.  ITIMER_REAL (a.k.a. the "wall" timer) might not
# run while the process is running.  For example, if the process is
# running in the kernel, the wall timer won't run.
#
# This test uses SIGALRM and not some other signal because we're
# testing the implementation of SIGALRM as a side effect of testing
# the ITIMER_VIRTUAL timer.
#
# The process should exit with status 0 if it ran for exactly 1 second.
# The process should exit with status 1
