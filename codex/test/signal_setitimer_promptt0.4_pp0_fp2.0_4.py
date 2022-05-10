import signal
# Test signal.setitimer()

def handler(sig, frame):
    print("Received signal", sig)
    signal.setitimer(signal.ITIMER_REAL, 0.5)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)

for i in range(10):
    time.sleep(0.5)
    print(".", end="", flush=True)

signal.setitimer(signal.ITIMER_REAL, 0)
print("\nDone")
