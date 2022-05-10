import signal
# Test signal.setitimer function
def receive_alarm(signum, stack):
    print 'Alarm :', time.ctime()

signal.signal(signal.SIGALRM, receive_alarm)
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)

while True:
    print 'not yet'
    time.sleep(1)
