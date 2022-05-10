import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Got signal", signum)
    if signum == signal.SIGALRM:
        print("SIGALRM")

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 1, 1)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)

for i in range(10):
    time.sleep(1)
    print(i)

signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0)

for i in range(10):
    time.sleep(1)
    print(i)
