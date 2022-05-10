import signal
# Test signal.setitimer()

# Set up the signal handler
def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Register the signal handler
signal.signal(signal.SIGALRM, handler)

# Define a function to be called
def do_something():
    print("Doing something")

# Call do_something() after a delay
signal.setitimer(signal.ITIMER_REAL, 5)

# Loop until a signal is received
while True:
    signal.pause()

# Set up the signal handler
def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Register the signal handler
signal.signal(signal.SIGALRM, handler)

# Define a function to be called
def do_something():
    print("Doing something")

# Call do_something() after a delay
signal.setitimer(signal.ITIMER_REAL, 5)

# Loop until a signal is received
while True:
    signal
