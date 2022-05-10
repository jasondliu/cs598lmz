import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print('Signal!')
    else:
        print('Signal! (no more timeouts)')

signal.signal(signal.SIGALRM, handler)
handler()

# Run the process.
print('Busy:', math.fsum(delays) * 1e6)
signal.pause()
