import signal
# Test signal.setitimer()

# Set up a signal handler
def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Register signal handler
signal.signal(signal.SIGALRM, handler)

# Define a function to test the timer
def test_timer():
    signal.setitimer(signal.ITIMER_REAL, 1)
    while True:
        signal.pause()

# Run the test
test_timer()

 
# Test signal.setitimer()

# Set up a signal handler
def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Register signal handler for signal.SIGALRM
signal.signal(signal.SIGALRM, handler)

# Define a function to test the timer
