import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print(len(delays))
        return
    for i in range(10):
        print('.')
        sys.stdout.flush()
        time.sleep(0.1)
    event.set()

event = threading.Event()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while not event.wait(1):
    print('+')
    sys.stdout.flush()
</code>

