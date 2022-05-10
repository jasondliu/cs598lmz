import signal
# Test signal.setitimer()
# pylint: disable=no-member

# NOTE: This test assumes the system has a working timerfd implementation.

def handler(signalnum, frame):
    print('Received signal', signalnum)
    raise Exception('Test exception')

signal.signal(signal.SIGALRM, handler)
signal.alarm(1)

# Create a timerfd
fd = os.timerfd_create(os.CLOCK_MONOTONIC, 0)

# Check that it doesn't have a thread yet
assert not sig_timer.has_timer(fd)

# Set itimer to fire in 1 second.
signal.setitimer(signal.ITIMER_REAL, 1, 0)

# Check that it now has a thread
assert sig_timer.has_timer(fd)

# Set itimer to fire in 10 seconds.
signal.setitimer(signal.ITIMER_REAL, 10, 0)

# Check that it still has a thread
assert sig_timer.has_timer(fd)

# Set
