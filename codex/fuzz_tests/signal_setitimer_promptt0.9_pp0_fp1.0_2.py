import signal
# Test signal.setitimer()
def handler(signum, frame):
    print "I'm waking up..."
    signal.setitimer(signal.ITIMER_REAL, 1)

def task():
    print "Starting task..."
    signal.setitimer(signal.ITIMER_REAL, 1, 1)
    while True:
        pass

def task_with_signal():
    print "Starting task #2..."
    signal.setitimer(signal.ITIMER_REAL, 1, 1)
    signal.signal(signal.SIGALRM, handler)
    while True:
        pass

# Test signal.alarm()
def handler_alarm(signum, frame):
    print "I'm waking up (signal.alarm)..."
    signal.alarm(1)

def task_alarm():
    print "Starting task with alarm..."
    signal.alarm(1)
    while True:
        pass

def task_alarm_with_signal():
    print "Starting task with alarm #2..."
    signal.al
