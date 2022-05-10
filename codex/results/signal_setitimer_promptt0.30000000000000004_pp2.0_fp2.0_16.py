import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

signal.alarm(0)

print("Done.")

# Test signal.setitimer()

def handler(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

signal.alarm(0)

print("Done.")

# Test signal.setitimer()

def handler(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, handler)

