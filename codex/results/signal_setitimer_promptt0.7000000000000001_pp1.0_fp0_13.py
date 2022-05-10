import signal
# Test signal.setitimer

def handler(signum, frame):
    print("Alarm", signum, "from", frame)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    # do some processing
    print(".", end="")
    time.sleep(0.5)
