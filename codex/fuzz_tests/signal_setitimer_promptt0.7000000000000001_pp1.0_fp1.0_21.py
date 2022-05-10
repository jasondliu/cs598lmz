import signal
# Test signal.setitimer()
def handler(signum, frame):
    print(signum)

signal.signal(signal.SIGALRM, handler)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)

while True:
    time.sleep(1)
