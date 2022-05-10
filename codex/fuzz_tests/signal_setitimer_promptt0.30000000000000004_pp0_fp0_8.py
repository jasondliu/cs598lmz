import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Received signal", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

print("Sleeping...")
time.sleep(0.5)
print("Done.")
