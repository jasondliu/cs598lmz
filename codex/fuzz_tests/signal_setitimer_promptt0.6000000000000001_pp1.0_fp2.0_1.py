import signal
# Test signal.setitimer()
def handler(signum, frame):
    print("Alarm")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
while True:
    time.sleep(1)
# End of test
</code>
I also tried to use <code>signal.ITIMER_VIRTUAL</code> and <code>signal.ITIMER_PROF</code>, but they don't work too.
Also I tried to use <code>signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)</code> and it works.
The question is: what <code>signal.SIGALRM</code> does not work with 0.2 seconds interval?
I'm using Python 3.7.3 on Windows 10 (1803).


A:

Try this instead:
<code>import signal
import time

def handler(signum, frame):
    print("Alarm")

signal.signal
