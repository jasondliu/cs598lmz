import signal
# Test signal.setitimer()

# First, use a handler that raises an exception.
# This can't be handled by the main program, so
# the whole process will die.

