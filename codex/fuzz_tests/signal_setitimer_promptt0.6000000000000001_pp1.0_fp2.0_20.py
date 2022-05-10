import signal
# Test signal.setitimer()
# ###########################################################################
# This is a test script for use with the setitimer() function.
#
# The test script registers a signal handler for SIGALRM, and then sets
# an interval timer for the alarm() function to fire every 5 seconds.
# The alarm() function is set to call the signal handler function,
# which prints out a message and resets the timer.
#
# This continues until the user enters "quit" at the keyboard.
# ###########################################################################

# Define SIGALRM handler function
def sigalrm_handler(signum, frame):
    # Print message and reset timer
    print("Interval timer expired.")
    signal.setitimer(signal.ITIMER_REAL, 5)

# Register the signal handler
signal.signal(signal.SIGALRM, sigalrm_handler)

# Set an interval timer
signal.setitimer(signal.ITIMER_REAL, 5)

# Wait for user input
while True:
    try:
        s = input("Enter 'quit' to exit: "
