import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)

# Set an alarm
signal.setitimer(signal.ITIMER_REAL, 2)

# This open() may hang indefinitely
fd = os.open('/dev/ptmx', os.O_RDWR)

# Check the alarm is still pending
print 'Sleeping for 1 second'
time.sleep(1)
print 'Alarm is still pending'

# This read() may hang indefinitely
os.read(fd, 1)

# Check the alarm is still pending
print 'Sleeping for 1 second'
time.sleep(1)
print 'Alarm is still pending'

# This close() may hang indefinitely
os.close(fd)

# Check the alarm is still pending
print 'Sleeping for 1 second'
time.sleep(1)
print 'Alarm is still pending'

# Check the alarm is still pending
print 'S
