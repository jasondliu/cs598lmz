import signal
# Test signal.setitimer() method
def alarm_handler(signum, stack):
    print('Alarm :', time.ctime())
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 3)
while True:
    print('tick')
    time.sleep(1)

# Test signal.setitimer() method
def alarm_handler(signum, stack):
    print('Alarm :', time.ctime())
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 3)
while True:
    print('tick')
    time.sleep(1)

# Test signal.setitimer() method
def alarm_handler(signum, stack):
    print('Alarm :', time.ctime())
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 3)
while True:
    print
