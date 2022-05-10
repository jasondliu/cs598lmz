import signal
# Test signal.setitimer() by setting a timer for 1 second, and then
# waiting for the timer to expire.
signal.alarm(1)
signal.pause()
