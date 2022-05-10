import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit(0)

# create an event for each child
def child():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while True:
        x = 1

# create a child process (or fork)
pid = os.fork()
if pid == 0:
    child()


while delays:
    time.sleep(1)

print(time.time() - start)
