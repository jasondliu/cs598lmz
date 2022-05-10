import signal
# Test signal.setitimer() and signal.getitimer()
#
# This test is not comprehensive, but it does test the functionality
# that the test_signal module uses.

def alarm_handler(signum, frame):
    print('Alarm')

signal.signal(signal.SIGALRM, alarm_handler)

signal.setitimer(signal.ITIMER_REAL, 0.2)
time.sleep(0.1)
signal.setitimer(signal.ITIMER_REAL, 0.2)
time.sleep(0.3)

print(signal.getitimer(signal.ITIMER_REAL))
signal.setitimer(signal.ITIMER_REAL, 0)
print(signal.getitimer(signal.ITIMER_REAL))

signal.setitimer(signal.ITIMER_REAL, 0.2)
time.sleep(0.1)
signal.setitimer(signal.ITIMER_REAL, 0)
time.sleep(0
