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
# This will probably interrupt the open() above, and the program will terminate

# If the open() returns, the alarm is disarmed and the following line will block
# indefinitely
os.write(fd, b'foo')

# Press Ctrl+C again to send a SIGINT and terminate the program

# The alarm() function is a simpler interface to setitimer()
# which only sets ITIMER_REAL and the interval timer
# signal.alarm(5)

# signal.setit
