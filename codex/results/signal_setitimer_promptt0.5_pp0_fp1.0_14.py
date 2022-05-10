import signal
# Test signal.setitimer()
def handler(sig, frame):
    print("Timeout")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass

# Test signal.signal()
def handler(sig, frame):
    print("Alarm")

signal.signal(signal.SIGALRM, handler)
signal.alarm(1)

while True:
    pass
