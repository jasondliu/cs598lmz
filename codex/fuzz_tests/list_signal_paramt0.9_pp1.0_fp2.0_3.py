import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("DONE")
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

while delays:
    try:
        s = select.select([], [], [], 2)
    except KeyboardInterrupt:
        print("Killing me softly")
        sys.exit(0)

print("Entering main loop...")
while True:
    try:
        print(".", end="", flush=True)
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("Killing me softly")
        break
