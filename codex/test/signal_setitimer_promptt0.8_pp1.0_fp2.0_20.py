import signal
# Test signal.setitimer(), use the C version of signal.setitimer() instead
# of the Python version.
#
# start timer to send a SIGALRM in 2 seconds,
# use signal handler to increment a global variable
# once timer goes off, 
# exit if sigalrm_count is 5
#
# repeat test several times
#
# NOTE:
# it is possible that the timer has not expired yet but the interpreter is
# already exiting. It is possible to get a signal handler called after
# the interpreter is already exiting.
