import signal
# Test signal.setitimer()

def handler(signum, frame):
    print(signum, frame)
    raise Exception("signal handler")

signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.signal(signal.SIGALRM, handler)

try:
    while True:
        pass
except:
    print("Caught!")
