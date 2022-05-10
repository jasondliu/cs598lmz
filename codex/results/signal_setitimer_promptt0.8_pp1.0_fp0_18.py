import signal
# Test signal.setitimer()
def alarm_handler(self, signum, frame):
	print "Caught alarm"
# Set up signal.signal() to catch SIGALRM
signal.signal(signal.SIGALRM, alarm_handler)
# Set the alarm
signal.setitimer(signal.ITIMER_REAL, 1.0, 0.5)
print "Starting the alarm..."
# Do some work
time.sleep(2.0)
print "Stopping the alarm..."
# Stop the alarm
signal.setitimer(signal.ITIMER_REAL, 0)
# Test signal.setitimer()
# Set up signal.signal() to catch SIGALRM
def alarm_handler(signum, frame):
	print "Caught alarm"
# Set the alarm
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
print "Starting the alarm..."
# Do some work
time.sleep(2.0)
print "Stopping the alarm..."
# Stop the alarm
signal.setitimer(sign
