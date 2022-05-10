import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays[0])
        del delays[0]

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays[0])

sum = 0.0
os.nice(19) # Don't hog the CPU
for i in range(N):
    sum += (time.time() * 1000 * 1000 * 1000) / 13763123.13
    signal.pause()

print(sum)
