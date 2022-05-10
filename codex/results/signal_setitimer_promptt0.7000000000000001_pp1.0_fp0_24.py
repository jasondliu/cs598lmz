import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 60)
#
# Set the signal handler and a 5-second alarm
#
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm

print 'Doing non-blocking I/O'
ret = os.read(fd, 1000)
print 'read() returned', len(ret)
