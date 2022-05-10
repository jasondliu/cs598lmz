import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Alarm handler called")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

while True:
    print("Waiting...")
    time.sleep(1)
