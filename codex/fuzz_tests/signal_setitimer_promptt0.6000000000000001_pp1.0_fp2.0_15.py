import signal
# Test signal.setitimer on linux
import sys
import time

# The setitimer call below works fine on Linux, but not on Windows.
# On Windows, it just doesn't do anything.
# This is the same on Python 2.7 and 3.x.
def signal_handler(signum, frame):
    print('Caught signal', signum)
    print('Sleeping for 5 seconds')
    time.sleep(5)
    print('Resuming')

signal.signal(signal.SIGALRM, signal_handler)

print('Setting timer for 3 seconds')
signal.setitimer(signal.ITIMER_REAL, 3, 0)
print('Waiting for timer to go off')
time.sleep(10)
print('Done')
</code>
On Windows, this prints:
<code>Setting timer for 3 seconds
Waiting for timer to go off
Done
</code>
On Linux, it prints:
<code>Setting timer for 3 seconds
Waiting for timer to go off
Caught signal 14
Sleeping for 5 seconds
Resuming
Done
</code
