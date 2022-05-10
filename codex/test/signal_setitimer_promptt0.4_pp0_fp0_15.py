import signal
# Test signal.setitimer()
#
# This test is only valid on platforms that support the ITIMER_REAL timer.
#
# ITIMER_REAL decrements in real time, and delivers SIGALRM upon expiration.
#
# This test verifies that the timer decrements in real time, and that the
# signal handler is invoked upon expiration.

# Timer expiration time, in seconds
TEST_TIME = 5

# Number of iterations to perform
ITERATIONS = 10

# Number of seconds to sleep between iterations
SLEEP_TIME = 5

# Flag set by signal handler
expired = False

# Signal handler for SIGALRM
def handler(signum, frame):
    global expired
    expired = True

# Install the signal handler for SIGALRM
signal.signal(signal.SIGALRM, handler)

# Perform the tests
for i in range(ITERATIONS):
    # Set the timer
    signal.setitimer(signal.ITIMER_REAL, TEST_TIME)

    # Wait for the timer to expire
    while not expired:
        pass


