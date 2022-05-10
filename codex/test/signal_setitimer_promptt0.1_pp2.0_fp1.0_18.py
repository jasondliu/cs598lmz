import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now to send a SIGINT before the alarm goes off

# After the alarm, a SIGALRM is sent and the signal handler is called
# with the exception that interrupts the open()

# Now we are back in the main program and can do other things
# Here are some that may hang if the open() is still blocked:
os.write(fd, 'Hello world\n')
os.close(fd)

# Press Ctrl+C again to interrupt the program

# The output of this program will vary depending on the timing of the
# signals and whether or not the open() call is interrupted.
# Here is one possible output:
#
