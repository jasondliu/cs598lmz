import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print_time()

signal.signal(signal.SIGALRM, handler)

def print_time():
    print(time.time())

signal.setitimer(signal.ITIMER_REAL, delays.pop())
print_time()
while delays:
    time.sleep(1e-10)
print_time()
