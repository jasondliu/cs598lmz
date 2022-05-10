import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

signal.signal(signal.SIGALRM, handler)

# Set up a 5-second alarm
signal.setitimer(signal.ITIMER_REAL, 5)

print("Before the sleep")
time.sleep(10)
print("After the sleep")
