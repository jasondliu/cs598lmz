import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
handler()

print("{0}{1}".format("Timer started: ", datetime.now()))
print("{0}{1}".format("Loop started: ", datetime.now()))

while True:
    pass
    # if not delays:
    #     break

print("{0}{1}".format("Loop stopped: ", datetime.now()))
