import signal
# Test signal.setitimer()
def handler(signum, frame):
    print("Received signal:", signum)
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    time.sleep(1)

# Test signal.setitimer()
def handler(signum, frame):
    print("Received signal:", signum)
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    time.sleep(1)

# Test signal.setitimer()
def handler(signum, frame):
    print("Received signal:", signum)
    signal.setitimer(signal.ITIMER_REAL,
