import signal
# Test signal.setitimer()

timeout = 5.0

def catch_alarm(signum, frame):
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, catch_alarm)

signal.setitimer(signal.ITIMER_REAL, timeout)

def wait_for_interrupt():
    signal.pause()

print 'Waiting', timeout, 'seconds for signal'
wait_for_interrupt()

print 'Exiting'
