import signal
# Test signal.setitimer function to check whether a
# SIGALRM signal will be sent to the program to terminate the loop.
# The main() shows the output and signals before the time
# is due. 'CTRL-C' needs to be used to force termination.
import time
import os

def signal_handler(signum, frame):
    global counts
    if signum == signal.SIGALRM:
        print("Good, SIGALRM is caught. signum = ", signum)
        print( "counts = ", counts)
    elif signum == signal.SIGINT:
        print("You broke out of the loop. Good job!")
        print("counts = ", counts)
        sys.exit(0)
    else:
        print("\nWhy are you here? signum = ", signum)
        print("counts = ", counts)
        sys.exit(1)

def main():
    # Set up the signal handler
    signal.signal(signal.SIGALRM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

