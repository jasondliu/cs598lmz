import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.setitimer(signal.ITIMER_REAL, 0)
signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    print "waiting..."
    time.sleep(.1)

print "Finished"
</code>


A:

I didn't fully understand the problem. But from what I read and understood, you can work around it with a thread:
<code>from threading import Thread
from random import uniform
from time import sleep

N = 5
delays = [uniform(0.000001, 0.000002) for i in range(N)]

def handler():
    for item in delays:
        print "Sleeping", item
        sleep(item)

handler_thread = Thread(target=handler)
handler_thread.start()
</code>

