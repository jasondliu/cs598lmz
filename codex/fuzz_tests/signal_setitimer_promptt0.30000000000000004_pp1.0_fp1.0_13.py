import signal
# Test signal.setitimer()
#
# This test is intended to be run in a child process.
#
# Test that signal.setitimer() works as expected.
#
# Python issue #8354:  setitimer() does not work on Windows.

def handler(signum, frame):
    print("handler")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Wait for a few signals
for i in range(3):
    signal.pause()

# Now disable the timer
signal.setitimer(signal.ITIMER_REAL, 0, 0)

# Wait for a few seconds to see if any more signals arrive.
time.sleep(1)

print("done")
