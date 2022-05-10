import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("done")
        sys.exit(0)

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)

while True:
    time.sleep(1)
</code>
The <code>signal.setitimer</code> method on Mac OS X is considerably less precise than the Linux ... equivalent (which itself is not very precise). I have found that I can get about ten times faster by polling instead of using a signal. 
I am considering some hack (or sort of) where I would do an initial measurement and then wait for that amount of time, and then wait for the next signal (i.e., if a timer happened to expire while I was running a handler, I would add it to the queue and signal myself). If I wait for the expected amount of time, then I can pick up all the missed signals, but this would open up a race condition (i.e., if I happen to wake up, handle a signal, and then fall asleep immediately, I will miss the next signal). 
It is
