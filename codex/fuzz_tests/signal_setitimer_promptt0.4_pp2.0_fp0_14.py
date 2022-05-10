import signal
# Test signal.setitimer()
#
# This test is intended to be run under the control of the
# testsuite, which will set the environment variable
# SLEEP_TIME to the number of seconds to sleep.

def handler(signum, frame):
    print 'handler'

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, float(os.environ['SLEEP_TIME']))
print 'sleeping'
time.sleep(2 * float(os.environ['SLEEP_TIME']))
print 'done'
