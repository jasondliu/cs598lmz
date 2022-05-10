import signal
# Test signal.setitimer(): timer
# stopped after a blocking system call
# in the handler.

class alarm_handler(object):
    def __init__(self):
        self.triggered = False

    def __call__(self, signum, frame):
        print 'received signal', signum
        self.triggered = True
        # Call a
        # non-interruptible system call
        time.sleep(1)

print 'setting up the timer'
ah = alarm_handler()
signal.signal(signal.SIGALRM, ah)

print 'setting the timer for 2 seconds'
signal.setitimer(signal.ITIMER_REAL, 2, 0)

print 'waiting for 3 seconds'
time.sleep(3)

print 'checking if timer was triggered'
if ah.triggered:
    print 'timer was triggered'
else:
    print 'timer was not triggered'
