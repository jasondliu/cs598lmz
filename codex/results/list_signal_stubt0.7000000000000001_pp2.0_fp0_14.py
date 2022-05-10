import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

# def set_timer(signum=None, frame=None):
#     if delays:
#         signal.setitimer(signal.ITIMER_REAL, delays.pop())

# signal.signal(signal.SIGALRM, set_timer)

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)

while delays:
    time.sleep(0.1)

print(time.time() - start)
