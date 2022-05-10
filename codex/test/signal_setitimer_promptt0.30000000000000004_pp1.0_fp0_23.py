import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print("Got alarm", signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    print("Sleeping")
    time.sleep(0.5)
    print("Done sleeping")
