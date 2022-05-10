import signal
# Test signal.setitimer()
def receive_alarm(signum, stack):
    print 'Alarm:', time.ctime()

signal.signal(signal.SIGALRM, receive_alarm)

signal.setitimer(signal.ITIMER_REAL, 1)
print "About to sleep for 5 seconds"
time.sleep(5)
print "Done sleeping"
