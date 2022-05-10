import signal
# Test signal.setitimer


def alarmhandler(signum, info=None):
    print 'got alarm'


signal.signal(signal.SIGALRM, alarmhandler)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
print 'sleeping'
time.sleep(0.531)
print 'done'
signal.alarm(0)
print 'uninstalled'
time.sleep(0.531)
print 'done2'
