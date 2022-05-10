import signal
# Test signal.setitimer()

# User signal handler
def handler(signum, frame):
    print("Signal handler called with signal", signum)
    print("Frame:", frame)

# Register signal handler
signal.signal(signal.SIGALRM, handler)

# Set the timer to go off
signal.setitimer(signal.ITIMER_REAL, 3.5)

# Wait for the timer to go off
print("Waiting for timer to go off...")
signal.pause()
print("Done.")
