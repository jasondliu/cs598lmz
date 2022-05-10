import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print('Done.')
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

print('Starting...')
while delays:
    signal.pause()
</code>
The script starts running, then the first timer fires after a random delay, then the second, and so on. Each timer fires in a different thread, and it takes too long to fire some of them. For example, the first one can take ~0.1 seconds, the second ~0.3 seconds, the third ~0.2 seconds, and so on.
If I replace <code>signal.pause()</code> with <code>time.sleep(1)</code>, the timers fire exactly after the specified delays, but the program spends too much time in <code>time.sleep()</code>.
I want to know if there is a way to wait for the
