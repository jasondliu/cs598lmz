import signal
# Test signal.setitimer(signal.ITIMER_REAL, 0, 1) fails
# It does not work on Mac or Linux, but it does not crash either
print "hello"
signal.setitimer(signal.ITIMER_REAL, 0, 1)
time.sleep(2)
print "would be nice to see this message"
time.sleep(1)
