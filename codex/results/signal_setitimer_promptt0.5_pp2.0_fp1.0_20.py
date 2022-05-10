import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Alarm", signum, frame)
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

print("Sleeping...")
time.sleep(3)
print("Done sleeping.")
