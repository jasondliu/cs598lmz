import signal
# Test signal.setitimer() and signal.getitimer()
# This test test the following functions:
#     signal.setitimer()
#     signal.getitimer()

# Create a new signal set
newset = signal.SignalSet(signal.SIGALRM)

# Add signal.SIGALRM to the signal set
newset.add(signal.SIGALRM)

# Block signal.SIGALRM
newset.block()

# Unblock signal.SIGALRM
newset.unblock()

# Set a handler for signal.SIGALRM
def handler(signum, frame):
    print("signal handler called with signal", signum)

signal.signal(signal.SIGALRM, handler)

# Set the timer to go off in 2 seconds
signal.setitimer(signal.ITIMER_REAL, 2)

# Wait for 5 seconds, then exit
