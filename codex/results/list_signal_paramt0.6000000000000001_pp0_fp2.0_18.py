import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)

# start the timer
handler()

# do something else
sys.stdout.write(".")
while delays:
    sys.stdout.flush()
    time.sleep(0.1)

print("done")
</code>
Now I would like to interrupt this program with a <code>SIGINT</code> (i.e. Ctrl+C) and have it print "interrupted" before terminating.  I tried this:
<code>import sys
import time
import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def interrupt(signum=None, frame=None):
    print("interrupted")
    sys.exit(0)

signal.signal
