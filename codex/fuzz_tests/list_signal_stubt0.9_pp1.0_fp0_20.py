import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

for sig in range(1, signal.NSIG):
    if sig in (signal.SIGKILL, signal.SIGSTOP):
        continue
    signal.signal(sig, handler)

handler(sig=signal.SIGALRM)

while delays:
    signal.pause()
