import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>
It runs fine most of the time, but sometimes it just seems to hang. I have to <code>kill -9</code> it to get it to quit. I've tried adding a <code>try</code>/<code>except KeyboardInterrupt:</code> before the <code>while</code> loop, but that doesn't seem to help.
Why does this script hang sometimes? Is there any way to fix it?
Edit: I'm only using Linux because I'm at work, but I'll test it on my Mac later.


A:

I think the problem is to do with Python's handling of signals.
I'm not very experienced in this area but, from what I've learned from the Python docs, it seems that there are two ways of handling signals: the old way (which is what the docs strongly recommend against) and the Pythonic way.
I'm running on Windows 7, so I
