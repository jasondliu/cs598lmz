import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Alarm handler called with signal", signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    print("Waiting...")
    time.sleep(0.5)

# EOF
