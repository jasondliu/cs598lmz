import signal
# Test signal.setitimer
#
# This program uses setitimer to set up a periodic timer that prints
# a message every few seconds, and then sleeps for a while.
#
# This program is started with a command line argument that specifies
# the number of seconds to sleep.  You can test the program by
# starting it in one window, and then switching to another window and
# typing "kill -USR1 <pid>" where <pid> is the process ID of the
# sleeping program.  This will cause the program to print a message
# and continue sleeping for the specified number of seconds.
#
# This program is meant to be used with the "kill" program, but it
# could be modified to use any signal-generating program.

# This function is called when a signal is received
def handler(signum, frame):
    print "Signal handler called with signal", signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang
