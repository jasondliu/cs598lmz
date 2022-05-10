import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    if delays:
        print(time.time(), 'delay', len(delays))
    else:
        print(time.time(), 'end')


signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    time.sleep(1000)
