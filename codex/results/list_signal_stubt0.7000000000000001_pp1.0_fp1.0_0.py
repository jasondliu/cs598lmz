import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, signal.SIG_DFL)
        print('SIGALRM signal handler restored to default')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

# Set a flag in a shared memory location, so that the main
# program knows that the alarm has gone off
import mmap
shared_memory = mmap.mmap(-1, 1)
shared_memory[0] = 0

# Wait for the alarm
while delays:
    time.sleep(1)

# If we reach this point, the alarm has gone off
print(shared_memory[0])
shared_memory[0] = 0

# Stop the alarm
signal.setitimer(signal.ITIMER_REAL, 0)
time.sleep(1)
print(shared_memory[0])
