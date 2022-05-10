import signal
# Test signal.setitimer()
# This test will run for about 10 seconds

def handler(signum, frame):
    print 'Signal handler called with signal', signum

for i in range(1, 5):
    print 'Setting alarm', i
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, i, 0)
    time.sleep(i + 1)
    signal.setitimer(signal.ITIMER_REAL, 0)
    print 'Sleeping', i
    time.sleep(i + 1)
print 'Done'
