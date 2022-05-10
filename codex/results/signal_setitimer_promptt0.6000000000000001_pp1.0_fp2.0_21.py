import signal
# Test signal.setitimer() and signal.getitimer()

def alarm_handler(signum, frame):
    print "Got alarm"

signal.signal(signal.SIGALRM, alarm_handler)

print "Setting itimer to 2 seconds"
signal.setitimer(signal.ITIMER_REAL, 2)
time.sleep(4)

print "Setting itimer to 0.5 seconds"
signal.setitimer(signal.ITIMER_REAL, 0.5)
time.sleep(4)

print "Setting itimer to 0 seconds"
signal.setitimer(signal.ITIMER_REAL, 0)
time.sleep(4)

print "Done"
