import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
callback = Callback()

print(f'{time.strftime("%H:%M:%S")}  Started! Waiting.')
with Watcher(callback):
    while delays:
        time.sleep(1)
