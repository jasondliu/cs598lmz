import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signum = signal.SIG_DFL
        signal.signal(signal.ITIMER_REAL, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.ITIMER_REAL, handler)

#while True:
#    pass
try:
    while True: pass
except KeyboardInterrupt:
    pass
</code>


A:

itimer fires every time (with probability of err < 1e-6), ignore the other answer.
the reason is quantum.
the quantum is too small to be seen on 'top'
quantum is about 20ms on my E3-1240 v3
run it for a couple minutes and see what happens.
the process will be churning 20ms at a shot and your handler will deliver the delays in 20ms chunks.
(haven't tested that lately, but I think that's what's going on)

