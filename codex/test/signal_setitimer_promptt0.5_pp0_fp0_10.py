import signal
# Test signal.setitimer
def handler(signum, frame):
    print("Alarm")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    pass

# Test signal.setitimer and signal.alarm
def handler(signum, frame):
    print("Alarm")

signal.signal(signal.SIGALRM, handler)
signal.alarm(1)

while True:
    pass

# Test signal.setitimer and signal.setitimer
def handler(signum, frame):
    print("Alarm")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    pass

# Test signal.setitimer and signal.alarm and signal.setitimer
def handler(signum, frame):
    print
