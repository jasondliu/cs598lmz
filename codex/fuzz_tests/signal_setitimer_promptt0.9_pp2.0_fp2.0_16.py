import signal
# Test signal.setitimer()

# Test the non-blocked mode
from TestSignals import alarm_occurred
signal.signal(signal.SIGALRM, alarm_occurred)
signal.setitimer(signal.ITIMER_REAL, 1)
for i in range(5):
    print('Sleeping %d seconds...' % i, end=' ')
    sys.stdout.flush()
    time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0)

print()
# Test the blocked mode
seconds = 2

print('Setting a %d-second timer...' % seconds)
signal.signal(signal.SIGALRM, alarm_occurred)
signal.setitimer(signal.ITIMER_REAL, seconds)
for i in range(3, 0, -1):
    print('Sleeping %d seconds...' % i)
    time.sleep(1)
print('Done.')
