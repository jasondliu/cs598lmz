import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)


signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>
This is, however, quite hard to understand and maintain.

If you want to do something similar, but with a more deterministic, predictable, and/or controllable behaviour, you can use a non-blocking <code>select</code> call, and then have a thread that waits for you to call <code>set_alarm</code> and then waits for the specified time and calls the callback.
<code>import select
import threading
import time

class Alarm:

    def __init__(self):
        self.waiters = set()
        self.lock = threading.Lock()
        self.callback = None
        self.running = True
        threading.Thread(target=self.
