import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1)

def receive_alarm(signum, stack):
    print 'Alarm :', time.ctime()

signal.signal(signal.SIGALRM, receive_alarm)

print 'Before:', time.ctime()
signal.pause()
print 'After :', time.ctime()

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)

def receive_alarm(signum, stack):
    print 'Alarm :', time.ctime()

signal.signal(signal.SIGALRM, receive_alarm)

print 'Before:', time.ctime()
signal.pause()
print 'After :', time.ctime()

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)

def receive_alarm(sign
