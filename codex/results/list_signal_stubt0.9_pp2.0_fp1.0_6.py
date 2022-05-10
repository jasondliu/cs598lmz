import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def f():
    for delay in delays:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(delay)

signal.signal(signal.SIGALRM, handler)
handler()

try:
    f()
except KeyboardInterrupt:
    print('\nExiting')
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
</code>
How can I pool once per a second and convert it to JSON?

