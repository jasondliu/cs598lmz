import signal
# Test signal.setitimer()

def handler(sig, frame):
    print("Alarm has been called")

signal.signal(signal.SIGALRM, handler)
print("Before setitimer")
signal.setitimer(signal.ITIMER_REAL, 0.5)
time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0)

print("\nAfter setitimer")
print("Sleeping for 1 seconds")
time.sleep(1)

# This can be used to see the timer working
# signal.setitimer(signal.ITIMER_REAL, 1)
