import signal
# Test signal.setitimer()
#
# The test is to set the timer to fire in 1 second, and then
# wait for the signal.
#
# This script is run by test_signal.py.

def handler(signum, frame):
    print('handler')
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

print('waiting')
signal.pause()
print('done')
