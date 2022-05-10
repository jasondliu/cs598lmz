import signal
# Test signal.setitimer()
def handler(signum, frame):
    print("In handler")
    return

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)
for i in range(1, 10):
    print("In main loop")
    time.sleep(1)

# Test signal.setitimer()
def handler(signum, frame):
    print("In handler")
    return

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
for i in range(1, 10):
    print("In main loop")
    time.sleep(1)
