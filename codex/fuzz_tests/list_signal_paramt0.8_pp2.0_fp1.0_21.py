import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print("Signal handler called with:", signum, frame)

# Register handler for 2 signals
signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)

# Tell the signal module to send the signal every 1 second
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
while delays:
    time.sleep(0.1)
