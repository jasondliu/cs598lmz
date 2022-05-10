import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, random.choice(delays), 0)
    else:
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

signal.signal(signal.SIGALRM, handler)
handler()

with open('/dev/null', 'wb') as f:
    while delays:
        f.write(str(delays.pop()).encode('utf-8'))
        f.write(b'\n')
        f.flush()
