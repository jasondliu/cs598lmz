import signal
# Test signal.setitimer()
#
# This program tests the signal.setitimer() function.
#
# It forks a child process which sets an interval timer to go off every
# five seconds and prints a message.  The parent process waits for a
# keyboard interrupt (control-C) and then sends a SIGALRM to the child
# process.  The child process catches the SIGALRM and exits.
#
# This test is not very rigorous.  It is possible for the child process
# to die before it can set the timer.  This is not very likely on a
# modern system with a fast processor.  If the child process dies before
# setting the timer, the parent process will wait forever for a SIGALRM
# that never comes.  This test will pass if you wait long enough for the
# child process to die or if you control-C the parent process.

# Get the signal numbers of SIGALRM and SIGINT.

SIGALRM = signal.SIGALRM
SIGINT = signal.SIGINT

# This function is called when a timer goes off.

def handler(signum, frame):
    print "
