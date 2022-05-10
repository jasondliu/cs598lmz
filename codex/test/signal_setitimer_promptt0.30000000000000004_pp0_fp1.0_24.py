import signal
# Test signal.setitimer()
#
# This test is a bit different from the other tests in this directory.
# It is a self-contained test that does not depend on any other tests
# and it is not run by the test runner.
#
# It is run by the test runner as a subprocess.
#
# The test runner will send a SIGALRM signal to this process
# after a certain amount of time.
#
# This test will set a timer for a shorter amount of time.
#
# If the timer fires before the SIGALRM signal is received,
# then the test passes.
#
# If the SIGALRM signal is received before the timer fires,
# then the test fails.
#
# This test is only run on Linux.
#
# The test runner will send a SIGALRM signal to this process
# after a certain amount of time.
#
# This test will set a timer for a shorter amount of time.
#
# If the timer fires before the SIGALRM signal is received,
# then the test passes.
#
# If the SIGALRM signal is received before the timer fires,
# then the test
