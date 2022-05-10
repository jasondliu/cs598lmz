import signal
# Test signal.setitimer() and signal.getitimer()

# This test is Linux-specific.
if sys.platform != 'linux':
    raise TestSkipped('Linux-specific test')

# The kernel has a resolution of 10 ms, so don't rely on a timer
# shorter than that.
TEST_TIMEOUT = 0.2

def handler(signum, frame):
    print('handler called')

signal.signal(signal.SIGALRM, handler)

# Test setitimer()
signal.setitimer(signal.ITIMER_REAL, TEST_TIMEOUT)
time.sleep(TEST_TIMEOUT * 2)

# Test getitimer()
signal.setitimer(signal.ITIMER_REAL, TEST_TIMEOUT)
time.sleep(TEST_TIMEOUT / 2)
print(signal.getitimer(signal.ITIMER_REAL))
time.sleep(TEST_TIMEOUT / 2)
print(signal.getitimer(signal.ITIMER_REAL))
