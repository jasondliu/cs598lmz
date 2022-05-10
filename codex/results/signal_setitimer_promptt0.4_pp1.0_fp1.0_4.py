import signal
# Test signal.setitimer()
#
# This test is for the case where a SIGALRM is delivered to a thread
# that has a signal handler for SIGALRM installed.
#
# This test is Linux specific and will fail on other platforms.

# This is a list of all the threads that are running.
threads = []

# This is a list of all the threads that have received a SIGALRM.
signalled_threads = []

# This is a list of all the threads that have received a SIGALRM and
# have had their signal handler called.
handled_threads = []

# This is a list of all the threads that have received a SIGALRM and
# have had their signal handler called and have returned from their
# signal handler.
returned_threads = []

# The number of threads to create.
num_threads = 10

# The number of seconds to wait for the threads to finish.
timeout = 10

# The number of seconds to wait for the threads to receive a SIGALRM.
alarm_timeout = 5

# The number of seconds to wait for the threads to have their signal

