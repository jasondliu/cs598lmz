import signal
# Test signal.setitimer by making a simple counter.
def handler(signum, frame):
    print("Signal handler called with signal", signum)

def counter(n):
    for i in range(n):
        time.sleep(1)
        print(i)
        # Call the signal handler.
        signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)

# Install the handler.
signal.signal(signal.SIGVTALRM, handler)

# Set the timer.
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)

# Start the counter.
counter(3)
