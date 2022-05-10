import signal
# Test signal.setitimer()
#
# This test checks the following:
#
# - SIGALRM is delivered to the main thread
# - signal.setitimer() works
# - signal.setitimer() can be used to cancel a pending timer
# - signal.setitimer() can be used to restart a timer
# - signal.setitimer() can be used to set a new timer
# - signal.setitimer() can be used to disable a timer
# - signal.setitimer() can be used to set a timer to zero
# - signal.setitimer() can be used to set a timer to a value greater than one
#
# This test is run by the "run-tests.py" script.

# Check that signal.setitimer() is available
try:
    signal.setitimer
except AttributeError:
    print('1..0 # SKIP signal.setitimer() not available')
    exit(0)

def handler(signum, frame):
    global handled
    handled = True

# Install a handler for SIGALRM
handled = False
signal.signal(signal
