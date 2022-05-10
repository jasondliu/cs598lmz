import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

print("I will print a dot every millisecond or so until {} dots have been printed or until you press Ctrl-C...".format(N))
while delays:
    signal.pause()
    print('.', end='', flush=True)

print("")
