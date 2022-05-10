import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while True:
    signal.pause()
</code>
(edit:) There are two things I want to point out:

If you don't want to use <code>signal.pause</code> you can busy wait and call <code>signal.setitimer</code> every time the signal fires. You also don't have to set the timer every time and can instead just sleep for the next delay and then call <code>signal.setitimer</code> for the timer that's due after that. In both cases signal dispatch becomes a task to be worked on and you can do other things, like servicing user input.
The busy waiting approach can be used in the threading case too, but read on for the full story.

(edit:) Just as a disclaimer: Disregard the next paragraph if you don't care about threading.

If you want to use threading, there are some details to consider. If you're doing something that blocks,
