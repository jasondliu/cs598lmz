import signal
# Test signal.setitimer()
#
# This program will run until it is killed using a signal.
#
# Usage:
#   python test_setitimer.py
#
# Then, in another window, kill the program using:
#   kill -s USR1 <pid>
#
# Where <pid> is the process ID of the test_setitimer.py program.

def signal_handler(signum, frame):
    print "Signal handler called with signal", signum

# Set the signal handler and a 5-second signal alarm
signal.signal(signal.SIGUSR1, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may or may not be necessary for your platform
fd = os.open('/dev/null', os.O_RDONLY)

# Loop until a signal is received
while 1:
    print "Waiting..."
    time.sleep(2)
