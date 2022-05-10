import signal
# Test signal.setitimer to generate SIGALRM timers.
#
# This test is Linux-specific for now, since we use the perf_event_open
# syscall to test the accuracy of the SIGALRM timer.
#
# We also assume the system has perf_event_open.
#
# The test has two phases.  In the first phase, we set a SIGALRM timer
# and measure how much time has elapsed between the time we set the
# timer, and the time we receive the SIGALRM signal.  We do this for
# several different values of interval.  We compare the actual elapsed
# time with the expected time.
#
# In the second phase, we run a loop where the SIGALRM handler
# repeatedly calls signal.setitimer to set a new timer, which should
# immediately fire.  We measure how much time has elapsed between the
# time we set the timer, and the time we receive the SIGALRM signal.
# We compare this against the expected time of 0.
#
# The results are printed to stdout in CSV format.
#
# Usage: setitimer_test.py [--quiet]

