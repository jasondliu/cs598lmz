import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)

while delays:
    t = time.time()
    signal.pause()
    # print(time.time() - t)
</code>
I replaced <code>signal.setitimer()</code> with <code>time.sleep()</code> in the <code>handler()</code> function, with the same results.


A:

If you want to use <code>signal.setitimer()</code>, you have to realize that <code>signal.setitimer()</code> is using real-time intervals! 
The <code>pause()</code> function — used in the second example — is using CPU time as a timer. So that's a rather different application.
To test the signal version, I have done the following:

unbuffered print with <code>time.clock()</code>
