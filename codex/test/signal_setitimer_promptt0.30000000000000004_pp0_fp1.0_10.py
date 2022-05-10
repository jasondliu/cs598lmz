import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print("Alarm")
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

while True:
    print("Tick")
    time.sleep(1)

# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print("Alarm")
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

while True:
    print("Tick")
    time.sleep(1)

# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print("Alarm")
    signal
