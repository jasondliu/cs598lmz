import signal
# Test signal.setitimer
#
# This test is for the case where the alarm goes off during the execution of
# the signal handler.
#
# The test is not very accurate.  We can't really control the order of
# execution of the alarm and the signal handler.  So, the test is just to
# ensure that the alarm does go off and that the handler does get called.

def handler(signum, frame):
    print("In handler")
    signal.setitimer(signal.ITIMER_REAL, 0.5, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)

print("In main")
time.sleep(2)
print("Done")
