import signal
# Test signal.setitimer()
#
# In this test, the child process sets a timer that will send a SIGALRM
# to the parent process after 1 second. The parent process sets a
# timer that will send a SIGALRM to the child process after 2 seconds.
# Both processes wait for their timers to go off. If both timers work,
# this test will terminate normally.
#
# If the parent process receives a SIGALRM before the child process,
# the test fails.
#
# If the child process receives a SIGALRM before the parent process,
# the test fails.
#
# If the child process does not receive a SIGALRM, the test fails.
#
# If the parent process does not receive a SIGALRM, the test fails.
#
# If the child process does not exit, the test fails.
#
# If the parent process does not exit, the test fails.
#
# If the parent process receives a SIGALRM after the child process,
# the test passes.
#
# If the child process receives a SIGALRM after the parent process,
# the test passes.
#
# If the child process
