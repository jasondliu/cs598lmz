import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print "No more delays"
        sys.exit(0)

signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.signal(signal.SIGALRM, handler)

while True:
    inp = raw_input("Press enter for next delay ")
    if inp:
        if inp == "q":
            break
        delays.append(float(inp))
</code>

